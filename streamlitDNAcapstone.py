def trainEval(model,xtrain,ytrain,bsize,epochs,xtest,ytest):
    batch_size=bsize
    historyTrain=model.fit(xtrain,ytrain,batch_size=bsize,epochs=epochs)
    historyEval=model.fit(xtrain,ytrain,batch_size=bsize,epochs=epochs,validation_data=(xtest,ytest))

def modelSequenceDNA(xtrain=x_train_array,ytrain=y_train_array,xtest=x_test_array,ytest=y_test_array,bsize=44,epochs=3,inputSize=33289,sizeHL=128,activnHL='exponential',activnOP='softmax',nLayers=3,nClass=2,opt='adam',loss='sparse_categorical_crossentropy',metrics=[keras.metrics.SparseCategoricalAccuracy(name='acc')]):
    model=tf.keras.Sequential()
    model.add(tf.keras.Input(shape=inputSize,))
    for i in range(nLayers):
        model.add(tf.keras.layers.Dense(sizeHL,activation=activnHL))
    model.add(layers.Dense(nClass,activation=activnOP))
    model.summary()
    model.compile(optimizer=opt,loss=loss,metrics=metrics)
    trainEval(model,xtrain,ytrain,bsize,epochs,xtest,ytest)
    return model   

def dnaInt(dnaCo):
    dnaVector=[]
    for i in dnaCo:
        dnaStr=''
        for j in i:
            if j=='A' or j=='a':
                dnaStr+='1'
            elif j=='C' or j=='c':
                dnaStr+='2'
            elif j=='T' or j=='t':
                dnaStr+='3'
            elif j=='G' or j=='g':
                dnaStr+='4'
            elif j=='N' or j=='n':
                dnaStr+='0'
            else:
                print('error')
        dnaVector.append(dnaStr)
    return dnaVector

def nu_tensor(dna_file):
    nu_tensor=[]
    for i in dna_file:
        tmp_narray=[]
        for j in i:
            tmp_narray.append(tf.convert_to_tensor(int(j)))
        nu_tensor.append(tmp_narray)
    return nu_tensor

def bufferDNA(dna,max=33289):
    buffDNA=[]
    #identify min-max
    dna_delta=abs(max-len(dna))
    stopCodonBuff='taa'*dna_delta:
    if len(dna)<max:
        buffDNA.append(dna+stopCodonBuff[:max-len(dna)]) 
    elif len(dna)==max:
        buffDNA.append(dna)
    else:
        print("dna of ALXgene is longer than max length of 33289 nucleotides. please pick a different bird...")
  #check lengths
    if len(buffDNA)==max:
        return buffDNA
    else:
        return 'error'

#sample streamlit file
import streamlit as st
import pandas as pd
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow import keras
import numpy as np

st.markdown('# Verify ID with DNA')
st.sidebar.markdown('# Verify unseen original face with DNA')

left_column,right_column=st.columns(2)

with left_column:
    chosen=st.sidebar.selectbox("Please guess type of feature this DNA visualizes", ["pointy","non-pointy"])
    st.write(f"You think owner of this DNA has a {chosen} feature.") 

with right_column:
    chosen=st.slider("Select probability that your guess is right",0,100,10)
    st.write(f"You are {chosen}% sure of your guess...")
    chosen=st.sidebar.selectbox("Would you like to verify guess?",["Yes","No"])
    if chosen=="Yes":
        #st.write("Please click on this button.") #to view code - st.code(get_file_content_as_string("streamlit_app.py"))
        st.write("Please upload DNA on feature of interest. File must be DNA sequence of ALXbird gene in a string of .txt file. For example \'actg...\'")
        uploaded_DNA=st.file_uploader("uploaded_file") 
        if uploaded_DNA is not None:
            if type(uploaded_DNA)==str:
                dataBuffDNAup=bufferDNA(uploaded_DNA)
                dataIntDNAup=dnaInt(dataBuffDNAup)
                dataNpDNAup=np.array(dataIntDNAup)
                dataTenDNAup=nu_tensor(dataNpDNAup)
                dataInputDNAup=np.array(dataTenDNAup)
                model=modelSequenceDNA(xtrain=xtrain.txt,ytrain=ytrain.txt,xtest=xtest.txt,ytest=ytest.txt)
                model.predict(dataInputDNAup)
             else:
                print("error DNA data is not a string")
    elif chosen=="No":
        st.write("Not so sure...would you like to reenter a guess?")

#sample streamlit file
import streamlit as st
import pandas as pd
import numpy as np
#from sklearn.cluster import OPTICS
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow import keras
import numpy as np
from sklearn.cluster import KMeans

#Source of data - referenced in https://www.ncbi.nlm.nih.gov/data-hub/taxonomy/57068/

#paper-zhang2014/chrW.GALGA.ACACH.maf at master · gigascience/paper-zhang2014 (github.com)

#https://www.nature.com/articles/518147a

#references
#https://www.ncbi.nlm.nih.gov/data-hub/taxonomy/57068/

def bufferDNA(dna):
    buffDNA=[]
    #identify min-max
    pdLens=pd.Series([len(i) for i in dna])
    dna_delta=pdLens.max()-pdLens.min()
    stopCodonBuff='taa'*dna_delta
    for idx,i in enumerate(dna):
        if len(i)<pdLens.max():
            buffDNA.append(i+stopCodonBuff[:pdLens.max()-len(i)])
        else:
            buffDNA.append(i)
  #check lengths
    len0=0
    barray=[]
    for idx,i in enumerate(buffDNA):
        if len0==0:
            len0=len(i)
        else:
            barray.append(len(i)==len0)
    sameLength=0
    for idx,i in enumerate(barray):
        if i:
            sameLength+=1
    if sameLength==len(dna)-1:
        return buffDNA
    else:
        return 'error'

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
 
st.markdown('# Verify ID with DNA')
st.sidebar.markdown('# Verify unseen original face with DNA')

left_column,right_column=st.columns(2)

with left_column:
    chosen=st.sidebar.selectbox("Please guess type of feature this DNA visualizes", ["pointy","non-pointy"])
    st.write(f"DNA probably visualizesEdited a {chosen} type of feature.") 

with right_column:
    chosen=st.slider("Select probability that your guess is right",0,100,10)
    st.write(f"You are {chosen}% sure of your guess...")
    chosen=st.sidebar.selectbox("Would you like to verify guess?",["Yes","No"])
    if chosen=="Yes":
        st.write("Please upload DNA on feature of interest. File must be DNA sequence of ALXbird gene in a string of .txt file. For example \'actg...\'")
        uploaded_DNA=st.file_uploader("uploaded_file") 
        if uploaded_DNA is not None:
            if type(uploaded_DNA)==str:
                #if len(xtrain_dataframed_app.iloc[:,0])==len(xtrain_dataframed.iloc[:,0])+1:
                #    st.write("File has been uploaded.")
                #else:
                #    st.write("please re-upload file.")             
                
                upDNA=pd.read_csv(uploaded_DNA) 
                xtrain_dataframed=pd.read_csv('xvar.txt')
                xtrain_dataframed_app_buff = bufferDNA(xtrain_dataframed_app) #buffer
                xtrain_dataframed_app_buff_int = dnaInt(xtrain_dataframed_app_buff)#int
                xtrain_dataframed_app_buff_int_np = np.array(xtrain_dataframed_app_buff_int)#np
                xtrain_dataframed_app_buff_int_np_ten = nu_tensor(xtrain_dataframed_app_buff_int_np)#tensor
                xtrain_dataframed_app = xtrain_dataframed.append(xtrain_dataframed_app_buff_int_np_ten)
                loaded_model = tf.keras.models.load_model('saved_model.pb')
                loaded_model.predict(xtrain_dataframed_app)
                kmeans=KMeans(n_clusters=2,random_state=0).fit(xtrain_dataframed)
                kmeans.predict(xtrain_dataframed_app_buff_int_np)
            else:
                print("error DNA data is not a string")
    elif chosen=="No":
        st.write("Not so sure...would you like to reenter a guess?")

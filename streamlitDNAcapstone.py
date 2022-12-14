#sample streamlit file
import streamlit as st
import pandas as pd
from sklearn.cluster import OPTICS
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow import keras
import numpy as np
import sklearn as sklearn
from sklearn.cluster import AffinityPropagation
from sklearn.svm import SVC

#Source of data - referenced in https://www.ncbi.nlm.nih.gov/data-hub/taxonomy/57068/

#paper-zhang2014/chrW.GALGA.ACACH.maf at master · gigascience/paper-zhang2014 (github.com)

#https://www.nature.com/articles/518147a

#references
#https://www.ncbi.nlm.nih.gov/data-hub/taxonomy/57068/

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
    st.write(f"DNA probably visualizes a {chosen} type of feature.") 

with right_column:
    chosen=st.slider("Select probability that your guess is right",0,100,10)
    st.write(f"You are {chosen}% sure of your guess...")
    chosen=st.sidebar.selectbox("Would you like to verify guess?",["Yes","No"])
    if chosen=="Yes":
        st.write("Please upload DNA on feature of interest. File must be DNA sequence of ALXbird gene in a string of .txt file. For example \'actg...\'")
        uploaded_DNA=st.file_uploader("uploaded_file") 
        if uploaded_DNA is not None:
            upDNA=pd.read_csv(uploaded_DNA) 
            print('uploaded data')
            st.write('uploaded data')
            #xtrain_dataframed=pd.read_csv('xvar.txt')
            #st.write('reading additional bird DNA data')
            #xtrain_data=pd.read_csv('dnaDataFrameRifleless10dec2022.txt') #without rifleman bird
            #st.write('reading training data')
            xtrain_data=pd.read_csv('tensorX_33000fourLRnp14Dec2022.txt') #all birds without rifleman
            st.write('reading x training data')
            ytrain_data=pd.read_csv('tensorY_33000fourLRnp.txt') #all birds without rifleman
            st.write('reading y training data')
            #xtrain_data.append(upDNA)
            #st.write('appending data')
            #training NN model - pending rest of model code
            #xtrain_dataframed_buff = bufferDNA(upDNA) #buffer ... might call this with .loc or .iloc
            #st.write('buffering DNA in processing model input')
            #xtrain_dataframed_buff_int = dnaInt(xtrain_dataframed_buff)#int
            #st.write('changing nucleotides to integers')
            #xtrain_dataframed_buff_int_np = np.array(xtrain_dataframed_buff_int)#np
            #st.write('going from Pandas dataframe to numeric py arrays')
            #xtrain_dataframed_buff_int_np_ten = nu_tensor(xtrain_dataframed_buff_int_np)#tensor
            #st.write('tensorizing...')
            #xtrain_dataframed_app = xtrain_dataframed.append(upDNA)#appending twice
            #st.write('appending new DNA data')
            ##loaded_model = tf.keras.models.load_model('https://drive.google.com/drive/folders/1wsRQkL4ecQr_ZtkQdwA7RFhh-0suDBwo?usp=share_link')
            #st.write('loading saved model')
            #loaded_model = tf.keras.models.load_model('')
            #loaded_model.predict(xtrain_dataframed_app)
            #st.write('predicting feature type based on DNA input in neural network model')
            #clustering=OPTICS(algorithm='ball_tree').fit(xtrain_data)
            #st.write('fitting model on OPTICS clustering')
            #clustering.labels_
            #if clustering.labels_[-1]==0:
                #st.write('printing OPTICS classifications')
            #    st.write("Your bird has a pointy beak")
            #else:
            #    st.write("Your bird has a not-so-pointy beak")
            #clusteringAP=AffinityPropagation(random_state=5).fit(nu_tensor(xtrain_dataframed))
            #st.write('fitting AffinityPropagation')
            #clusteringAP.labels_
            #st.write('printing labels on cluster')
            #SVC
            modelSVCtrain=SVC(gamma='auto',probability=True,class_weight='balanced',break_ties=True)
            modelSVCtrain.fit(xtrain_data,ytrain_data)
            predictSVC=modelSVCtrain.predict([upDNA.iloc[:,0]])
            #GradientBoostingClassifier
            #gbc43reload=GradientBoostingClassifier(criterion='squared_error').fit(tensorX_33000lessrifleNPreload,tensorY_33000lessrifleNPreload)
            #predictGBC43reload=gbc43reload.predict([upDNA.iloc[:,0]])
            if predictSVC[0]<=2: 
                st.write('Your bird has a pointy beak')
            else:
                st.write('Your bird has a not-so-pointy beak')
    elif chosen=="No":
        st.write("Not so sure...would you like to reenter a guess?")

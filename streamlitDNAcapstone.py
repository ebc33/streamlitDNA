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
            xtrain_data=pd.read_csv('tensorX_33000fourLRnp14Dec2022.txt') #all birds without rifleman
            st.write('reading x training data')
            ytrain_data=pd.read_csv('tensorY_33000fourLRnp.txt') #all birds without rifleman
            st.write('reading y training data')
            modelSVCtrain=SVC(gamma='auto',probability=True,class_weight='balanced',break_ties=True)
            modelSVCtrain.fit(xtrain_data,ytrain_data)
            predictSVC=modelSVCtrain.predict([upDNA.iloc[:,0]])
            if predictSVC[0]<=2: 
                st.write('Your bird has a pointy beak')
            else:
                st.write('Your bird has a not-so-pointy beak')

#sample streamlit file
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import OPTICS

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
        st.write("Please upload DNA on feature of interest. File must be DNA sequence of ALXbird gene in a string of .txt file. For example \'actg...\'")
        uploaded_DNA=st.file_uploader("uploaded_file") 
        if uploaded_DNA is not None:
            if type(uploaded_DNA)==str:
                upDNA=pd.read_csv(uploaded_DNA)
                xtrain_dataframed=pd.read_csv('xvar.txt')
                xtrain_dataframed_app=xtrain_dataframed.append(upDNA)
                if len(xtrain_dataframed_app.iloc[:,0])==len(xtrain_dataframed.iloc[:,0])+1:
                    st.write("File has been uploaded.")
                    clusteringOptics=OPTICS(min_samples=2).fit(xtrain_dataframed_app)
                    if clusteringOptics.labels_[-1]<=0:
                        st.write("your bird has a non-pointy beak")
                    elif clusteringOptics.labels_[-1]>0:
                        st.write("your bird has a pointy beak")
                else:
                    st.write("please re-upload file.")              
            else:
                print("error DNA data is not a string")
    elif chosen=="No":
        st.write("Not so sure...would you like to reenter a guess?")

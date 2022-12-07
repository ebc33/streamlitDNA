#sample streamlit file
import streamlit as st
import pandas as pd
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
        st.write("Please upload DNA on feature of interest. File must be of .txt or .csv type")
        uploaded_DNA=st.file_uploader("uploaded_file") 
        if uploaded_DNA is not None:
            dataDNAup=pd.read_csv(uploaded_DNA)
            st.write(dataDNAup)
    elif chosen=="No":
        st.write("Not so sure...would you like to reenter a guess?")

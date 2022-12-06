#sample streamlit file
import streamlit as st
st.markdown('# Main Page')
st.sidebar.markdown('# Main Page')

left_column,right_column=st.columns(2)

with left_column:
    chosen=st.sidebar.selectbox("Please select your guess on type of feature this DNA visualizes", ["pointy","non-pointy"])
    st.write(f"You think the owner of this DNA has a {chosen} feature.") 

with right_column:
    chosen=st.sidebar.slider("Select probability that your guess is right",(0,100,50))
    st.write(f"You are {chosen}% sure of your guess...")
    chosen=st.sidebar.selectbox("Would you like to verify guess?",["Yes","No"])
    if chosen=="Yes":
        st.write("Please click on this button.") #to view code - st.code(get_file_content_as_string("streamlit_app.py"))
    elif chosen=="No":
        st.write("Not so sure...would you like to reenter a guess?")

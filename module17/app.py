from optparse import Option

import streamlit as st

col1,col2,col3,col4,col5=st.columns(5, gap="small",vertical_alignment="center")

with col1:
    st.header("colum 1")
    st.write("contents for colum 1")

with col2:
    st.header("colum 2")
    st.write("contents for colum    2")

with col3:
    st.header("colum 3")
    st.write("contents for colum    3")

with col4:
    st.header("colum 4")
    st.write("contents for colum    4")

with col5:
    st.header("colum 5")
    st.write("contents for colum    5")

with st.container():
    st.header("dsa")
    st.write("asd")

st.write("wer")


st.sidebar.header("sidebar")
st.sidebar.write("dfghj")
st.sidebar.selectbox("select an option", ["Option1","Option2","Option3"])

with st.form

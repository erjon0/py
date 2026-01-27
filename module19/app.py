import pandas as pd
import streamlit as st
import plotly.express as plt

books_df = pd.read_csv("bestsellers_with_categories_2022_03_27.csv")

st.title('ddssad')
st.write('dsadas')

st.sidebar.header('dsadas')
with st.sidebar.form('dsadsa'):
    new_name = st.text_input('dasadas')
    new_name = st.text_input("sadda")
    new_user_rating = st.slider("sadsa",0.0,5.0,0.1)
    new_reviews =  st.number_input('eewqewq', min_val=0 , step=1)
    new_price = st.number_input('dsadsa' , min_value=0 , step=1)
    new_year = st.number_input('dasdas', min_value=2009, max_value=2026)
    new_geanre = st.checkbox('dsadsa', books_df['dsadsad'].unique())
    submit_button = st
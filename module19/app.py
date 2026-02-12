import pandas as pd
import streamlit as st
import plotly.express as plt

from module18.app import total_books, unique_titles, average_rating, top_titles

books_df = pd.read_csv("bestsellers_with_categories_2022_03_27.csv")

st.title('ddssad')
st.write('dsadas')

st.sidebar.header('dsadas')
with st.sidebar.form('dsadsa'):
    new_name = st.text_input('dasadas')
    new_author = st.text_input("sadda")
    new_user_rating = st.slider("sadsa",0.0,5.0,0.1)
    new_reviews =  st.number_input('eewqewq', min_val=0 , step=1)
    new_price = st.number_input('dsadsa' , min_value=0 , step=1)
    new_year = st.number_input('dasdas', min_value=2009, max_value=2026)
    new_genre = st.checkbox('dsadsa', books_df['dsadsad'].unique())
    submit_button = st.form_sumbit_button()


if selected_author != 'all':
    filtered_book_df = filtered_book_df[filterd_books_df['author'] == selected_author]
if selected_year != 'all':
    filtered_book_df = filtered_book_df[filterd_books_df['Year'] == selected_author]
if selected_author != 'all':
    filtered_book_df = filtered_book_df[filterd_books_df['geanre'] == selected_author]

filtered_book_df  = filtered_book_df[
    (filtered_book_df['user rating' >= min_rateig] & (filtered_book_df['price'] <= ))
]

st.subheader('summay statisics')
total_books = filtered_book_df.shape[0]
unique_title = filtered_book_df['name'].nununiqe()
average_rating = filtered_book_df['user rating'].mean()
average_price  = filtered_book_df['price'].mean()

col1, col2, col3, col4 = st.columns(4)
col1.metric('totlal books', total_books)
col2.metric('unique titles', unique_titles)
col3.metric('avrage rating', avrage_rating)
col4.metric('avreage price', average_price)

col1, col2 = st.columns(2)

with col1:
    st.subheader('dsadsadas')
    top_titles = filtered_book_df['name'].valve_counts().head(10)
    st.bar_chart(top_titles)
with col2:
    st.subheader('sadsadsad')
    top_authors = filtered_book_df['author'].value_counts().head(10)
    st.bar_chart(top_authors)


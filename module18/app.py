import pandas as pd
import streamlit as st
import plotly.express as px

st.header('defghjk')

df = pd.DataFrame({
    'Name':['vlera','Andi','darisi'],
    'age':[24,27,16],
    'City':['dsa','dasdas','dsa']
})

st.write(df)

st.title("Best selling book ")
st.title('dasdas')

books_df = pd.read_csv('module18/bestsellers_with_categories_2022_03_27.CVS')

st.subheader('sumary statistics')

total_books =  books_df.shape[0]
unique_titles = books_df['name'].nunique()
average_rating = books_df['user rating'].mean()
average_price = books_df['price'].mean()

col1,col2,col3,col4 = st.columns(4)
col1.metric('total books', total_books)
col2.metric('unique titles',unique_titles)
col3.metric('average rating'f'{average_rating:2f}')
col4.metric('average price'f'${average_price:.2f}')

st.subheader('dsadsa')
st.write(books_df.head())

col1,col2 =  st.columns(2)

with col1:
    st.subheader('dsaads')
    top_titles = books_df['name'].value_counts().head(10)
    st.bar_chart(top_titles)

with col2:
    st.subheader('top 10')
    top_titles = books_df['name'].value_counts().head(10)
    st.bar_chart(top_titles)

st.subheader('dasdsadasdas')
size = books_df.groupby(['year','ganre']).size().reset_index(names='counts')

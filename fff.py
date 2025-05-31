import streamlit as st
import pandas as pd
import random
from PIL import Image






# Load the CSV file
@st.cache_data
def load_data():
    return pd.read_csv('Book_Dataset_1.csv')

df = load_data()

def recommend_book(genre):
    # Filter by genre (case insensitive)
    genre_books = df[df['Category'].str.lower() == genre.lower()]
    
    if genre_books.empty:
        return None
    
    # Pick a random book
    random_book = genre_books.sample().iloc[0]
    return random_book

# Streamlit app
st.title("📚 Book Recommender")
genre=st.selectbox("selcet the book",df['Category'])


if genre:
    book = recommend_book(genre)
    ddd=book['Title']
    
    if book is not None:
        st.subheader("Recommended Book")
        st.write(f"**Title:** {book['Title']}")
        st.write(f"**Genre:** {book['Category']}")
        img=df[df['Title']==ddd]['Image_Link'].values[0]
        st.image(img,width=160)
         

    else:
        st.error(f"No books found for genre: {genre}")

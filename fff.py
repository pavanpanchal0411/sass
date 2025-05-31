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

import base64


def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background("k.jpg")  # Replace with your image file

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

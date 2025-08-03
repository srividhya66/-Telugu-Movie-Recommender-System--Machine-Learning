import streamlit as st
from model import load_data, create_similarity_matrix, recommend


st.set_page_config(page_title="Telugu Movie Recommender", layout="centered")
st.title("🎬 Telugu Movie Recommender")

# Load data and compute similarity
movies = load_data()
similarity = create_similarity_matrix(movies)

# User selects a movie
selected_movie = st.selectbox("🎥 Choose a Telugu movie:", movies['title'].values)

# Show recommendations
if st.button("🔍 Recommend"):
    recommendations = recommend(selected_movie, movies, similarity)
    st.subheader("🍿 You may also enjoy:")
    for movie in recommendations:
        st.write("👉", movie)

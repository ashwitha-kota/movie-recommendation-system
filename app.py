# app.py
import streamlit as st
import pickle
import pandas as pd

# -------------------------------
# 1️⃣ Load Pickle Files
# -------------------------------
with open('artifacts/movie_dict.pkl', 'rb') as f:
    movie_dict = pickle.load(f)
movies = pd.DataFrame(movie_dict)

with open('artifacts/similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

# -------------------------------
# 2️⃣ Recommendation Function
# -------------------------------
def recommend(movie):
    if movie not in movies['title'].values:
        return ["Movie not found in dataset!"]
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = [movies.iloc[i[0]].title for i in movie_list]
    return recommended_movies

# -------------------------------
# 3️⃣ Streamlit App Layout
# -------------------------------
st.title("🎬 Movie Recommender System")

# Dropdown to select movie
selected_movie = st.selectbox(
    "Select a Movie:",
    movies['title'].values
)

# Recommend button
if st.button("Show Recommendations"):
    recommendations = recommend(selected_movie)
    st.write("Top 5 similar movies:")
    for i, rec in enumerate(recommendations, start=1):
        st.write(f"{i}. {rec}")

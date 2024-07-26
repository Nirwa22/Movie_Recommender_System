import streamlit as st
import pickle
Movie_list = pickle.load(open('Movie.pkl', 'rb'))
Movies = Movie_list.values
Similarity = pickle.load(open('Similarity.pkl', 'rb'))
st.title("MOVIE RECOMMENDER SYSTEM")


def recommend(movie):
    movie_index = Movie_list[Movie_list['title'] == movie].index[0]
    t = sorted(list(enumerate(Similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for j in t:
        recommended_movies.append(Movie_list.iloc[j[0]].title)
    return recommended_movies


Selected_Movie = st.selectbox("Enter the Movie", Movies)
if st.button('Recommend'):
    for i in recommend(Selected_Movie):
        st.write(i)

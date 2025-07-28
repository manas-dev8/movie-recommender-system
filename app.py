import streamlit as st
import pickle
import pandas as pd
# import requests

# def fetch_poster(movie_id):
#   response = requests.get('https://api.themoviedb.org/3/movie/{movie.id}?api_key=<<api_key>>&language=en-US'.format(movie_id))
#     data = response.json()
# return "image path" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:8]

    recommended_movies = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        # fetch poster from api

        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
'What movies do you like?',
movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)

        # https://api.themoviedb.org/3/movie/{movie.id}?api_key=<<api_key>>&language=en-US
        # 8265bd167966a7ea12ac168da84d2e8
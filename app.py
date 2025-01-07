import streamlit as st
import pickle
import pandas as pd
import requests
import base64

def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=546174a1d124123a3080c3abce8d4b8f')
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/" + data['poster_path'], data.get('genres', [])

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:10]

    recommended_movies = []
    recommended_movies_posters = []
    recommended_movies_tags = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        title = movies.iloc[i[0]].title
        poster, tags = fetch_poster(movie_id)
        recommended_movies.append(title)
        recommended_movies_posters.append(poster)
        recommended_movies_tags.append(tags)
    return recommended_movies, recommended_movies_posters, recommended_movies_tags

def set_background(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpeg;base64,{encoded_string}");
            background-size: cover;
        }}
        .movie-title {{
            width: 150px;
            text-align: center;
            white-space: normal;
            word-wrap: break-word;
            font-size: 14px;
            font-weight: bold;
            margin-top: 5px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('ScreenSuggest')

set_background("C:/Users/shiva/OneDrive/Desktop/python/Movie_recommendation_system/movie1.jpg")

selected_movie_name = st.selectbox(
    "Select a movie to get recommendations:",
    movies['title'].values
)

if st.button('Recommend'):
    names, posters, tags = recommend(selected_movie_name)
    selected_movie = None
    for i in range(0, len(names), 4):
        col1, spacer1, col2, spacer2, col3, spacer3, col4 = st.columns([1, 0.1, 1, 0.1, 1, 0.1, 1]) 

        with col1:
            st.image(posters[i], width=150)
            st.markdown(f"<div class='movie-title'>{names[i]}</div>", unsafe_allow_html=True)

        if i + 1 < len(names):
            with col2:
                st.image(posters[i + 1], width=150)
                st.markdown(f"<div class='movie-title'>{names[i + 1]}</div>", unsafe_allow_html=True)

        if i + 2 < len(names):
            with col3:
                st.image(posters[i + 2], width=150)
                st.markdown(f"<div class='movie-title'>{names[i + 2]}</div>", unsafe_allow_html=True)

        if i + 3 < len(names):
            with col4:
                st.image(posters[i + 3], width=150)
                st.markdown(f"<div class='movie-title'>{names[i + 3]}</div>", unsafe_allow_html=True)

    if selected_movie is not None:
        st.markdown("### Movie Details")
        st.write("**Title:**", names[selected_movie])
        st.write("**Genres:**", ", ".join([genre['name'] for genre in tags[selected_movie]]))

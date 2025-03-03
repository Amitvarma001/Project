import streamlit as st
import pickle
import pandas as pd


def recommend(movie):
    movie_index=movies[movies["title"]==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x: x[1])[1:6]

    recommended_movies=[]
    for i in movie_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies



# Open the pickle file in read-binary ('rb') mode
with open("movie_dict.pkl", "rb") as file:
    movie_dict = pickle.load(file)  # Correct way to load a pickle file
import pickle
similarity = pickle.load(open('\\AI And ML\\similarity.pkl', 'rb'))
print(type(similarity))
print(similarity.shape if hasattr(similarity, "shape") else similarity.keys())

movies=pd.DataFrame(movie_dict)

st.title("Movie Recomment System")

selected_movie_name=st.selectbox(
    "how would you like to contacted?",
    movies["title"].values)

if st.button("Recommend"):
   recommendation= recommend(selected_movie_name)
   for i in recommendation:
      st.write(i)
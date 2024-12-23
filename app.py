# import streamlit as st
# import pandas as pd
# import numpy as np
# import os
# import Recommenders as Recommenders

# # Load data
# @st.cache
# def load_data():
#     song_df_1 = pd.read_csv('triplets_file.csv')
#     song_df_2 = pd.read_csv('song_data.csv')
#     song_df = pd.merge(song_df_1, song_df_2.drop_duplicates(['song_id']), on='song_id', how='left')
#     song_df['song'] = song_df['title'] + '-' + song_df['artist_name']
#     return song_df

# # Initialize recommenders
# @st.cache(allow_output_mutation=True)
# def initialize_recommenders(song_df):
#     pr = Recommenders.popularity_recommender_py()
#     pr.create(song_df, 'user_id', 'song')

#     ir = Recommenders.item_similarity_recommender_py()
#     ir.create(song_df, 'user_id', 'song')

#     return pr, ir

# # Load data and models
# song_df = load_data()
# pr, ir = initialize_recommenders(song_df)

# # Streamlit App
# st.title("Music Recommendation System")

# menu = ["Popularity-Based", "Item Similarity"]
# choice = st.sidebar.selectbox("Select Recommendation Type", menu)

# if choice == "Popularity-Based":
#     st.subheader("Popularity-Based Recommendations")
#     user_id = st.text_input("Enter User ID", "")
#     if st.button("Recommend"):
#         if user_id:
#             recommendations = pr.recommend(user_id)
#             st.write(recommendations)

# elif choice == "Item Similarity":
#     st.subheader("Item Similarity Recommendations")
#     user_id = st.text_input("Enter User ID", "")
#     if st.button("Recommend"):
#         if user_id:
#             recommendations = ir.recommend(user_id)
#             st.write(recommendations)

# # Allow user to find similar songs
# st.subheader("Find Similar Songs")
# input_songs = st.text_input("Enter Song Names (comma-separated)", "")
# if st.button("Find Similar Songs"):
#     if input_songs:
#         song_list = [song.strip() for song in input_songs.split(",")]
#         similar_songs = ir.get_similar_items(song_list)
#         st.write(similar_songs)


import streamlit as st
import pandas as pd
import numpy as np
import os
import Recommenders as Recommenders

# Load data
@st.cache_data
def load_data():
    song_df_1 = pd.read_csv('triplets_file.csv')
    song_df_2 = pd.read_csv('song_data.csv')
    song_df = pd.merge(song_df_1, song_df_2.drop_duplicates(['song_id']), on='song_id', how='left')
    song_df['song'] = song_df['title'] + '-' + song_df['artist_name']
    return song_df

# Initialize recommenders
@st.cache_resource
def initialize_recommenders(song_df):
    pr = Recommenders.popularity_recommender_py()
    pr.create(song_df, 'user_id', 'song')

    ir = Recommenders.item_similarity_recommender_py()
    ir.create(song_df, 'user_id', 'song')

    return pr, ir

# Load data and models
song_df = load_data()
pr, ir = initialize_recommenders(song_df)

# Streamlit App
st.title("Music Recommendation System")

menu = ["Popularity-Based", "Item Similarity"]
choice = st.sidebar.selectbox("Select Recommendation Type", menu)

if choice == "Popularity-Based":
    st.subheader("Popularity-Based Recommendations")
    user_id = st.text_input("Enter User ID", "")
    if st.button("Recommend"):
        if user_id:
            recommendations = pr.recommend(user_id)
            st.write(recommendations)

elif choice == "Item Similarity":
    st.subheader("Item Similarity Recommendations")
    user_id = st.text_input("Enter User ID", "")
    if st.button("Recommend"):
        if user_id:
            recommendations = ir.recommend(user_id)
            st.write(recommendations)

# Allow user to find similar songs
st.subheader("Find Similar Songs")
input_songs = st.text_input("Enter Song Names (comma-separated)", "")
if st.button("Find Similar Songs"):
    if input_songs:
        song_list = [song.strip() for song in input_songs.split(",")]
        similar_songs = ir.get_similar_items(song_list)
        st.write(similar_songs)

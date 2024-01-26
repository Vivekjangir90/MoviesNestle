import requests
import streamlit as st
import pandas as pd
import json

def app():
    st.text("hiiiii")




def page1():
    # Read genres from JSON file
    gens = pd.read_json("genres.json")
    genres= gens["name"].tolist()
    genres_id = gens["id"].tolist()
    selected_genres = st.multiselect("Select genres", genres)
    toggle_button_genres = st.checkbox("Much Include genres")
    gen_code = []
    def name_to_gen_id():
        for i in selected_genres:
                for num, j in enumerate(genres):
                    if i == genres[num]:
                        gen_code.append(genres_id[num])
    if toggle_button_genres:
        name_to_gen_id()
        params["with_genres"] = ",".join(str(genre) for genre in gen_code)
    else:
        name_to_gen_id()
        params["with_genres"] = "&".join(str(genre) for genre in gen_code)


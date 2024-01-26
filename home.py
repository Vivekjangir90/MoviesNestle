import requests
import streamlit as st
import pandas as pd
import base64
import json

page_number = 1
def app():
    global page_number
    include_video = []
    sort_by = "popularity.desc"
    include_adult = []
    # logo = st.image("Logo.png", width=355)
    # col1= st.columns([1])
    # with col1:
    #     logo
    
    # custom_html = """
    # <div class="custom-class">
    #     <img src="Logo.png" alt="Your Image">
    #     <p>Your Caption</p>
    # </div>
    # """
    # st.markdown(custom_html, unsafe_allow_html=True)


    # logo_path = "Logo.jpg"
    with open( "style.css" ) as css:
        st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
    
    def get_img_as_base64(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    
    Logo = get_img_as_base64("Logo.png")
    # page_size = 
    custom_html = f"""
        <div  style="text-align: left;">
            <img class="logo_css"  src="data:image/png;base64,{Logo}" alt="Logo" ;
                     ">
        </div>
    """

    st.markdown(custom_html, unsafe_allow_html=True)

    logo_css = """
        <style>

        .st-emotion-cache-1bkljio {
            position: absolute;
            background: rgb(0, 0, 0);
            color: rgb(236, 228, 236);
            inset: 0px;
            color-scheme: dark;
            overflow: hidden;
            border: 0px solid;
            border-image: linear-gradient(to right, violet, indigo, blue, green, yellow, orange, red);
            border-image-slice: 1;
            animation: rainbow-animation 5s linear infinite;

        </style>

    """
    st.write(logo_css, unsafe_allow_html=True)


    gens = pd.read_json("genres.json")
    genres= gens["name"].tolist()
    genres_id = gens["id"].tolist()
    selected_genres = st.multiselect("Select genres", genres)

    gen_code = []
    def name_to_gen_id():
        for i in selected_genres:
                for num, j in enumerate(genres):
                    if i == genres[num]:
                        gen_code.append(genres_id[num])

    # for years
    years = list(range(2024, 1800, -1))
    selected_years = st.selectbox("Select years", years,None)
    # params["primary_release_year"] =selected_years

    #for cast data
    data  = pd.read_json("popular.json")
    casts= data["name"].tolist()
    casts_id= data["id"].tolist()
    selected_casts = st.multiselect("Select casts", casts)

    cast_code = []
    def name_to_cast_id():
        for i in selected_casts:
                for num, j in enumerate(casts):
                    if i == casts[num]:
                        cast_code.append(casts_id[num]) 

    name_to_gen_id()
    genres = ",".join(str(genre) for genre in gen_code)
    name_to_cast_id()
    cast = ",".join(str(cast) for cast in cast_code)

    # Get results from tmdb discover api
    def discover_movies():
        global page_number
        url = "https://api.themoviedb.org/3/discover/movie?api_key=1b46d8d88c680c018f026ea039d36f98&include_adult=false&include_video=false&page={}&primary_release_year={}&sort_by=popularity.desc&with_cast={}&with_genres={}".format(page_number,selected_years,cast,genres)
        response = requests.get(url)
        response= response.json()
        # st.text(response)
        # st.text(url)
        # return response

        title_m = [x["title"] for x in response['results']]
        post_m = [x["poster_path"] for x in response['results']]
        raw_num = len(title_m) // 5 + 1
        a = 0

        grid = st.checkbox("Grid")
        if grid:
            st.title(":rainbow[Movies]")
            posters = [f"https://image.tmdb.org/t/p/w500{poster}" if poster is not None else None for poster in post_m]
            image_gap = 20
            image_width = 150
            image_height = 200

            container_html = f"""
            <style>
                .custom-container {{
                    

                    display: flex;
                    flex-wrap: wrap;
                    gap: {image_gap}px;
                    justify-content: center;
                    
                }}
                .custom-image {{
                    flex: 0 0 {image_width}px;
                    max-width: 100%;
                    height: {image_height}px;
                    margin: auto auto 60px auto;
                    border: 2px solid;
                    border-image: linear-gradient(to right, violet, indigo, blue, green, yellow, orange, red);
                    border-image-slice: 1;
                    animation: rainbow-animation 5s linear infinite;

                }}
            </style>
            <div class="custom-container">
                {''.join([
                    f'<div class="custom-image"><img src="{poster}" width="100%" height="100%"><p>{title}</p></div>'
                    if poster is not None
                    else f'<div class="custom-image"><img src="https://github.com/Vivekjangir90/YBI_ML_PROJECTS/raw/main/poster_img.jpg" width="100%" height="100%"><p>{title}</p></div>'
                    for poster, title in zip(posters, title_m)
                ])}
            </div>
            """

            st.write(container_html, unsafe_allow_html=True)

        else:
            st.title(":rainbow[Movies]")
            for j in range(raw_num):
                with st.container():
                    cols = st.columns([1, 1, 1, 1, 1])
                    for i, nam in enumerate(title_m[a:a + 5]):
                        with cols[i]:
                            try:
                                if (nam and post_m[a+i]) is not None:
                                    st.text(nam)
                                    st.image("https://image.tmdb.org/t/p/w500/{}".format(post_m[a + i]))
                                elif (post_m[a + i] is None) and (nam is not None) :
                                    st.text(nam)
                                    st.image("https://github.com/Vivekjangir90/YBI_ML_PROJECTS/raw/main/poster_img.jpg")
                                elif (post_m[a + i] is not None) and (nam is None):
                                    st.text("Unknown")
                                    st.image("https://image.tmdb.org/t/p/w500/{}".format(post_m[a + i]))
                                else:
                                    st.text("nam")
                                    st.image("https://github.com/Vivekjangir90/YBI_ML_PROJECTS/raw/main/poster_img.jpg")
                            except Exception as e:
                                pass                  
                    a += 5

        url = "https://api.themoviedb.org/3/discover/tv?api_key=1b46d8d88c680c018f026ea039d36f98&first_air_date_year={}&include_adult=false&include_null_first_air_dates=false&language=en-US&page={}&sort_by=popularity.desc&with_genres={}".format(selected_years,page_number,genres)
        response = requests.get(url)
        response= response.json()
        # st.text(response)
        # st.text(url)
        # return response

        title_m = [x["name"] for x in response['results']]
        post_m = [x["poster_path"] for x in response['results']]
        raw_num = len(title_m) // 5 + 1
        a = 0
        if grid:
            st.title(":rainbow[Web Series]")
            posters = [f"https://image.tmdb.org/t/p/w500{poster}" if poster is not None else None for poster in post_m]
            image_gap = 20
            image_width = 150
            image_height = 200

            container_html = f"""
            <style>
                .custom-container {{
                    display: flex;
                    flex-wrap: wrap;
                    gap: {image_gap}px;
                    justify-content: center;
                }}
                .custom-image {{
                    flex: 0 0 {image_width}px;
                    max-width: 100%;
                    height: {image_height}px;
                    margin: auto auto 60px auto;
                }}
            </style>
            <div class="custom-container">
                {''.join([
                    f'<div class="custom-image"><img src="{poster}" width="100%" height="100%"><p>{title}</p></div>'
                    if poster is not None
                    else f'<div class="custom-image"><img src="https://github.com/Vivekjangir90/YBI_ML_PROJECTS/raw/main/poster_img.jpg" width="100%" height="100%"><p>{title}</p></div>'
                    for poster, title in zip(posters, title_m)
                ])}
            </div>
            """

            st.write(container_html, unsafe_allow_html=True)

        else:
            st.title(":rainbow[Web Series]")
            for j in range(raw_num):
                with st.container():
                    cols = st.columns([1, 1, 1, 1, 1])
                    for i, nam in enumerate(title_m[a:a + 5]):
                        with cols[i]:
                            try:
                                if (nam and post_m[a+i]) is not None:
                                    st.text(nam)
                                    st.image("https://image.tmdb.org/t/p/w500/{}".format(post_m[a + i]))
                                elif (post_m[a + i] is None) and (nam is not None) :
                                    st.text(nam)
                                    st.image("https://github.com/Vivekjangir90/YBI_ML_PROJECTS/raw/main/poster_img.jpg")
                                elif (post_m[a + i] is not None) and (nam is None):
                                    st.text("Unknown")
                                    st.image("https://image.tmdb.org/t/p/w500/{}".format(post_m[a + i]))
                                else:
                                    st.text("nam")
                                    st.image("https://github.com/Vivekjangir90/YBI_ML_PROJECTS/raw/main/poster_img.jpg")
                            except Exception as e:
                                pass                  
                    a += 5


    # if st.button("results"):
    #     page_number = 1
    #     st.text(page_number)
    #     discover_movies()


    if page_number >= 1:
        discover_movies()
        
    if page_number > 1:
        if st.button("previous"):
            page_number = max(1, page_number - 1)  # Corrected line
            st.rerun()
            # discover_movies()

    if page_number >= 1:
        if st.button("next"):
            page_number += 1
            # st.text(page_number)
            st.rerun() 
            st.text(page_number)



import requests
import streamlit as st
import pandas as pd
import json
import base64

# Initialize session state
if 'page_number' not in st.session_state:
    st.session_state.page_number = 1

def app():
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

    url = "https://api.themoviedb.org/3/discover/tv?api_key=1b46d8d88c680c018f026ea039d36f98&include_adult=false&include_null_first_air_dates=false&page=1&sort_by=primary_release_date.desc&with_original_language=hi&page={}".format(st.session_state.page_number)

    response = requests.get(url)
    response = response.json()
    # print_movies(response)
    # return response

    title_m = [x.get("name") for x in response.get('results') if x.get("name") and x.get("poster_path")]
    post_m = [x.get("poster_path") for x in response['results'] if  x.get("name") and x.get("poster_path")]
    raw_num = len(title_m) // 5 + 1
    a = 0

    if st.checkbox("Grid View"):
        posters = [f"https://image.tmdb.org/t/p/w500{i}" for i in post_m if i is not None]
        # st.image(posters, width=120, caption=[name for name in title_m], use_column_width=False)
        # Set the gap between images
        # image_gap = 100  # Adjust the gap as needed
        
        image_gap = 20 # Adjust the gap as needed
        image_width = 150
        image_height = 200
        bottom_margin = 20
        top_margin = 20
        # Build HTML and CSS for the container
        container_html =f"""
    <style>
        body {{
            margin: 100px; /* Remove default body margin */
            padding: 100px; /* Remove default body padding */
            margin-top: 100px; /* Remove top margin */
        }}
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
            margin: auto auto 30px auto  ;
            border: 2px solid;
            border-image: linear-gradient(to right, violet, indigo, blue, green, yellow, orange, red);
            border-image-slice: 1;
            animation: rainbow-animation 5s linear infinite;

        }}
    </style>
    <div class="custom-container">
        {''.join([f'<div class="custom-image"><img src="{poster}" width="100%" height="100%"><p>{title}</p></div>' for poster, title in zip(posters, title_m)])}
    </div>
"""


        # Display the container using st.write with allow_html=True
        st.write(container_html, unsafe_allow_html=True)
    else:
        for j in range(raw_num):
            with st.container():
                cols = st.columns([1, 1, 1, 1, 1])
                for i, nam in enumerate(title_m[a:a + 5]):
                    with cols[i]:
                        try:
                            if nam is not None:
                                st.text(nam)
                                st.image("https://image.tmdb.org/t/p/w500/{}".format(post_m[a + i]))
                        except Exception as e:
                            pass
                        
                a += 5


    if st.session_state.page_number == 1:
        if st.button("next"):
            st.session_state.page_number += 1
            st.rerun()
    else:
        if st.button("previous"):
            st.session_state.page_number = max(1, st.session_state.page_number - 1)  # Corrected line
            st.rerun()
        if st.button("next"):
            st.session_state.page_number += 1
            st.rerun()



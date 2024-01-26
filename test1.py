import streamlit as st
import requests

# Initialize session state
if 'page_number' not in st.session_state:
    st.session_state.page_number = 1

def app():

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
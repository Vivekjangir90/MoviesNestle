import streamlit as st
import requests
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



    url = "https://api.themoviedb.org/3/movie/now_playing?language=en-US&page={}".format(st.session_state.page_number)

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxYjQ2ZDhkODhjNjgwYzAxOGYwMjZlYTAzOWQzNmY5OCIsInN1YiI6IjY1YTdmNzM0Mzg3NjUxMDEzMDFhNmViZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.XGohA1BMLe83L_GR87D6hI8B2HVtdR0zpuJeizbH9_8"
    }

    response = requests.get(url, headers=headers)
    response = response.json()

    title_m = [x["title"] for x in response['results'] if ("title" in x and x["title"]) and ("poster_path" in x and x["poster_path"])]
    post_m = [x["poster_path"] for x in response['results'] if ("title" in x and x["title"]) and ("poster_path" in x and x["poster_path"])]
    raw_num = len(title_m) // 5 + 1
    a = 0
    if st.checkbox("Grid View"):
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

        for j in range(raw_num):
            with st.container():
                cols = st.columns([1, 1, 1, 1, 1])
                for i, nam in enumerate(title_m[a:a + 5]):
                    with cols[i]:
                        try:
                            if (nam and path_m[a+i]) is not None:
                                st.text(nam)
                                st.image("https://image.tmdb.org/t/p/w500/{}".format(post_m[a + i]))
                        except Exception as e:
                            pass
                        
                a += 5

    url = "https://api.themoviedb.org/3/tv/popular?language=en-US&page={}".format(st.session_state.page_number)

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxYjQ2ZDhkODhjNjgwYzAxOGYwMjZlYTAzOWQzNmY5OCIsInN1YiI6IjY1YTdmNzM0Mzg3NjUxMDEzMDFhNmViZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.XGohA1BMLe83L_GR87D6hI8B2HVtdR0zpuJeizbH9_8"
    }



    response = requests.get(url, headers=headers)
    response = response.json()
    # st.text(response)

    title_m = [x["name"] for x in response['results'] if ("name" in x and x["name"]) and ("poster_path" in x and x["poster_path"])]
    post_m = [x["poster_path"] for x in response['results'] if ("name" in x and x["name"]) and ("poster_path" in x and x["poster_path"])]
    raw_num = len(title_m) // 5 + 1
    a = 0
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


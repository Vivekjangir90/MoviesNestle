import streamlit as st
from streamlit_option_menu import option_menu
import home,search, trending, popular, top_rated, bollywood_movie,bollywood_web,action, comedy, horror, sci_fi, thriller, rate_us, about
import base64


# with open( "style.css" ) as css:
#     st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

st.set_page_config(
    layout="wide",
    initial_sidebar_state="expanded",
    
)


custom_style = """
    <style>
        .st-emotion-cache-t3xdah {
            font-size: 80px;  /* Adjust the font size as needed */
        }
    </style>
"""

# Render the custom style
st.markdown(custom_style, unsafe_allow_html=True)

w_out_css = """
<style>
        .st-emotion-cache-1v0mbdj {
            width: calc(20% - 1rem);
            flex: 1 1 calc(20% - 1rem);
            border-radius: 10px; /* Adjust the border radius as needed */
            border: 2px solid;
            border-image: linear-gradient(to right, violet, indigo, blue, green, yellow, orange, red);
            border-image-slice: 1;
            animation: rainbow-animation 5s linear infinite;
    }
</style>
"""
st.write(w_out_css, unsafe_allow_html=True)

custom_css = """
        <style>
        body {
            margin: auto;
            font-size:40px;
            font-family: -apple-system, BlinkMacSystemFont, sans-serif;
            overflow: auto;
            background: linear-gradient(315deg, #4f2991 3%, #7dc4ff 38%, #36cfcc 68%, #a92ed3 98%);
            animation: gradient 15s ease infinite;
            background-size: 400% 400%;
            background-attachment: fixed;
        }
        .custom-image {
        
    
    </style>
"""

# Apply the custom CSS
# st.markdown(custom_css, unsafe_allow_html=True)






# Initialize session state
if 'page_number' not in st.session_state:
    st.session_state.page_number = 1
    st.session_state.button_states = {'previous_button': False, 'next_button': False}


# @st.cache_data
#def get_img_as_base64(file):
#    with open(file, "rb") as f:
#        data = f.read()
#    return base64.b64encode(data).decode()


#img = get_img_as_base64("image.jpg")
#img1 = get_img_as_base64("image1.jpeg")

"""
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
# background-image: url("https://images.unsplash.com/photo-1501426026826-31c667bdf23d");
# background-image: url("data:image/png;base64,{img1}");

background-size: 180%;
background-position: fit;
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stSidebar"] > div:first-child {{
# background-image: url("data:image/png;base64,{img}");
background-position: left; 
background-repeat: no-repeat;
background-attachment: fixed;
}}
[data-testid="stMarkdownContainer"] > div:data-testid="stMarkdownContainer" {{
font_size = 24px;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

"""



class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        # Custom CSS style for sidebar container
        custom_sidebar_css = """
            <style>
                .st-emotion-cache-16txtl3 {
                padding: 6rem 1.5rem;
                background-color: black;
                /* outline: none; */
                outline-color: black;
                border-color: black;
                font-size:30px;
            }
                }
            </style>
        """

        # Apply the custom CSS to the sidebar
        st.markdown(custom_sidebar_css, unsafe_allow_html=True)


        # Apply the custom CSS to the sidebar
        # st.markdown(custom_sidebar_css, unsafe_allow_html=True)

        with st.sidebar:
            app = option_menu(
                menu_title='Main Menu ',
                options=['HOME', "Search Here", 'Trending Movies', 'Popular Movies', 'Top Rated Movies',"Bollywood Movies","Bollywood Web", 'Action Movies', 'Comedy Movies', 'Horror Movies', 'Sci-Fi Movies', 'Thriller Movies', 'Rate Us','About'],
                icons=['house-fill', 'search', 'easel', 'easel', 'easel', 'collection-play', 'collection-play', 'display', 'display', 'display', 'display', 'display', 'star', 'chat-text-fill'],
                default_index=0,
                # orientation="horizontal",
                styles={
                    "container": { "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "24px"},
                    "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "0px",
                                "--hover-color": "#C36F09"},
                    "nav-link-selected": {"background-color": "#C46F07"},
                    
                }
            )

        for app_entry in self.apps:
            if app == app_entry["title"]:
                app_entry["function"].app()

if __name__ == "__main__":
    multi_app = MultiApp()

    multi_app.add_app("HOME", home)
    multi_app.add_app("Search Here", search)
    multi_app.add_app("Trending Movies", trending)
    multi_app.add_app("Popular Movies", popular)
    multi_app.add_app("Top Rated Movies", top_rated)
    multi_app.add_app("Bollywood Movies", bollywood_movie)
    multi_app.add_app("Bollywood Web", bollywood_web)
    multi_app.add_app("Action Movies", action)
    multi_app.add_app("Comedy Movies", comedy)
    multi_app.add_app("Horror Movies", horror)
    multi_app.add_app("Sci-Fi Movies", sci_fi)
    multi_app.add_app("Thriller Movies", thriller)
    multi_app.add_app("Rate Us", rate_us)
    multi_app.add_app("About", about)
    # multi_app.add_app("Advance Search", advance_search)

    multi_app.run()

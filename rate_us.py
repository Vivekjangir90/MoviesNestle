import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
import base64

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
    st.title("Rate Us")


    # Establishing a Google Sheets connection
    conn = st.connection("gsheets", type=GSheetsConnection)

    # Fetch existing vendors data
    existing_data = conn.read(worksheet="rating", usecols=list(range(3)), ttl=5)
    existing_data = existing_data.dropna(how="all")

    # st.dataframe(existing_data)
    # Display a message to the user
    st.write("We'd love to hear your feedback. Please rate your experience below.")

    with st.form(key="rate us"):
        user_name = st.text_input("Enter Your Name*")

        rate_us = st.radio("Give Rating Us  👉*",

                options=[":star::star::star::star::star:", ":star::star::star::star:", ":star::star::star:", ":star::star:", ":star:"],
        )
        comment = st.text_area("Comments", "")
        # st.markdown("**required*")

        submit_button = st.form_submit_button(label="Submit")
    if rate_us == ":star::star::star::star::star:":
        rate_us = 5
    elif rate_us == ":star::star::star::star:":
        rate_us = 4
    elif rate_us == ":star::star::star:":
        rate_us = 3
    elif rate_us == ":star::star:":
        rate_us = 2
    else:
        rate_us = 1

    if submit_button:
        if  (user_name and rate_us) is  None:
            st.text("fill your name please!")
            st.stop()
        else:
            # Update Google Sheets with the new vendor data
            rating = pd.DataFrame([
            {
            "Name" : user_name,
            "Rating" : rate_us,
            "Comment" : comment
            
            }
            
            ])
            updated_df= pd.concat([existing_data,rating], ignore_index=True)
            conn.update(worksheet="rating", data=updated_df)

            st.success(f"Thank you {user_name} for your rating of {rate_us} stars!")
            st.success("rating details successfully submitted!")

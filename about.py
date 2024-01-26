import streamlit as st
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




    # Heading
    st.title("Welcome to MovieNestle")
    st.subheader("Your go-to destination for an unparalleled cinematic experience!")

    # Introduction
    st.write("Hello, I'm **Vivek Jangir**, and together with my talented team, we've crafted a platform designed to "
             "**revolutionize the way you explore and enjoy movies and web series**.")

    # Discover and Recommend
    st.header("Discover and Recommend:")
    st.write("Are you looking for the perfect movie or web series to dive into? Look no further! Our website offers an "
             "extensive filtration and search system, allowing you to find the ideal content tailored to your preferences. "
             "Whether you're in the mood for a gripping thriller, a heartwarming drama, or a laugh-out-loud comedy, we've got you covered.")

    # Recommendation Hub
    st.header("Recommendation Hub:")
    st.write("But that's not all – we believe that movie recommendations are best when they come from those who truly know your "
             "taste. Our platform empowers anyone, including you, to share personalized recommendations. Whether you want to suggest "
             "a hidden gem to a friend or find something new for yourself, our recommendation hub is the place to be.")

    # Robust Filtration Options
    st.header("Robust Filtration Options:")
    st.write("Navigate through our vast collection with ease using our advanced filtration options. Filter movies and web series by "
             "genres, cast, and release year, ensuring that you find exactly what you're looking for. Our user-friendly interface "
             "provides a seamless experience, making the exploration process enjoyable and efficient.")

    # Team Behind the Magic
    st.header("Team Behind the Magic:")
    st.write("I'm proud to introduce the creative minds behind **MovieNestle**. **Jaikishan Badgujar**, an artist known for his work "
             "in \"*Jay Kixxn*\", has lent his design expertise to ensure a visually stunning and user-friendly interface. **Dinesh Bisnoi**, "
             "the technical wizard from \"*SVYAMKRIT*\", has tackled the technical aspects, ensuring a smooth and responsive platform.")

    # Connect with Us
    st.header("Connect with Us:")
    st.write("At **MovieNestle**, we're not just a platform; we're a community of movie enthusiasts. Join us, share your favorite picks, "
             "and explore recommendations from others. Connect with us on social media, and let's build a community that shares the love "
             "for great storytelling.")

    st.subheader("Contact Information:")
    st.markdown("- **Vivek Jangir**: [Mobile](+919024950465) | [Email](mailto:vivekjangir90@gmail.com)")
    st.markdown("- **Jaikishan Badgujar**: [Instagram](https://www.instagram.com/jay_kixxn/)")
    st.markdown("- **Dinesh Bisnoi**: [Instagram](https://www.instagram.com/lord_svyamkrit/)")

    # Conclusion
    st.write("Embrace the future of entertainment with **MovieNestle**. We're not just a website; we're an experience. Start your cinematic journey today!")


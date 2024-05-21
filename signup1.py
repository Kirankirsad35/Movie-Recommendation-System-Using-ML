import http
import webbrowser
from idlelib import window

import streamlit as st
from streamlit.components.v1 import html
import hashlib
from streamlit_option_menu import option_menu
import sqlite3

conn = sqlite3.connect('data.db')
c = conn.cursor()

def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data


def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data


with st.sidebar:
    choose = option_menu("Menu", ["About Project",  "Sign Up", "Login"],
                         icons=['book', 'kanban', 'person lines fill','person lines fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "black"},
        "icon": {"color": "red", "font-size": "25px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": ""},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )

if choose == 'About Project':
    st.title("Movie Recommendation System")
    html_string = "<p><b><h5>Movie recommendation systems provide a mechanism to assist users in classifying users with similar interest. Recommender systems are information filtering tools that aspire to predict the rating for users and items, predominantly from big data to recommend their likes.Movie recommendation system is developed using Agile methodology<br/><br/> The recommendation system analyzes the past preferences of the user concerned, and then it uses this information to try to find similar movies. This information is available in the database (e.g., lead actors, director, genre, etc.). After that, the system provides movie recommendations for the user. That said, the core element in content-based filtering is only the data of only one user that is used to make predictions.Movie recommendation engine works by suggesting movies to the user based on the metadata information. The similarity between the movies is calculated and then used to make recommendations. For that, our text data should be preprocessed and converted into a vectorizer using the Count Vectorizer, KNN, matrix factorization.Machine learning project are implemented using python in jupyter software with listed libraries Pandas, numpy, SKlearn.<h5/><b/></p> "
    st.markdown(html_string, unsafe_allow_html=True)


if choose == 'Sign Up':
    st.subheader("Create New Account")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password", type='password')
    if st.button("Signup"):
        if new_user == "" and new_password == '':
            my_js = """
                           alert("Please fill the input fields!")    
                             """
            my_html = f"<script>{my_js}</script>"
            html(my_html)
        elif new_user == "" or new_password == '':
            my_js = """
              alert("Please fill the input fields!")    
                                    """
            my_html = f"<script>{my_js}</script>"
            html(my_html)
        create_usertable()
        add_userdata(new_user, make_hashes(new_password))
        st.success("You have successfully created a valid Account")
        st.info("Go to Login Menu to login")

if choose == 'Login':
    st.subheader("Login into Account")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password", type='password')
    a = [new_user,new_password]
    if st.button("Login"):

        if new_user == "" and new_password=='':
            my_js = """
                    alert("Please fill the input fields!")   

                      """
            my_html = f"<script>{my_js}</script>"
            html(my_html)
        elif new_user == "" or new_password == '':
                my_js = """
                        alert("Please fill the input fields!")    
                          """
                my_html = f"<script>{my_js}</script>"
                html(my_html)
        else:
            create_usertable()
            add_userdata(new_user, make_hashes(new_password))
            my_js = """
                alert("Login Successful!")
                  
                """
            my_html = f"<script>{my_js}</script>"
            html(my_html)
            if st.success:
                webbrowser.open('http://localhost:8501/')

            else:
              st.errors("Incorrect User Name or Password")

def add_bg_from_url():
    st.markdown(
         f"""
         
         
         <style>
         .stApp {{
             background-image: url("https://www.thetechgame.com/images/news/article/593d51b692.png");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()



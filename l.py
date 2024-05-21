import streamlit as st
from streamlit_option_menu import option_menu

with st.sidebar:
    choose = option_menu("Menu", ["About project",  "Project Planning", "Sign Up", "Login"],
                         icons=['menu', 'kanban', 'person lines fill','person lines fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "25px"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": ""},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )


def login():
    if choose == ("MENU",['Login']):
        st.write("")
import sqlite3
conn = sqlite3.connect('data.db')
c = conn.cursor()


# Security
#passlib,hashlib,bcrypt,scrypt
import hashlib
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


def main():
	"""Simple Login App"""

	st.title("Simple Login App")

	menu = ["Home","Login","SignUp"]
	choice = st.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Movie Recommendations Login Credentials")

	elif choice == "Login":


		username = st.text_input("User Name")
		password = st.text_input("Password",type='password')
		if st.button("Login"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:

				st.success("Logged In as {}".format(username))
				st.write("Click Here(http://localhost:8502/) for Movie Recommendation System Project")
			else:
				st.warning("Incorrect Username/Password")





	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')
		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")








if __name__ == '__main__':
	main()


import streamlit as st
import pandas as pd
# DB Management
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
				st.write("Click Here(http://localhost:8502/)for")
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



def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://repository-images.githubusercontent.com/275336521/20d38e00-6634-11eb-9d1f-6a5232d0f84f");
             background-attachment: fixed;
             background-size: cove
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

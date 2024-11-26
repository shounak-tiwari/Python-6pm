#create a user and password validation using function 

#import re module for matching username is matched from user regex or not 

import re

def ValidationSignIn():
	user_name = input("Enter the user name : ")
	password = input("Enter the password : ")
	user_regex = r"^[A-Za-z][A-Za-z0-9_]{7,29}$"
	password_regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+={}[\]:;\"'<>,.?/\\|`~]).{8,}$"

	if re.match(user_regex,user_name):
		print("Name is valid ")
	else:
		print("Enter valid user_name")


	if re.match(password_regex,password):
		print("password is valid")

	else:
		print("password enter again ")

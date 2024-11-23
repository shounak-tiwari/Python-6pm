from re import match 

def form_validation():
	first = input('Enter the first name of student : ')
	last = input('Enter the last name of student : ')
	email = input('Enter the email : ')

	first_regex = r'^[A-Za-z]{2,25}$'  # Matches a name with 2–25 alphabetic characters
	email_regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'  # Matches an email

	if match(first_regex,first):
		print("name is correct")	
		if match(email_regex,email):
			return "email is correct"
		else:
			return "email not valid please provide valid email"
	else:
		return "first name is not correct please enter correct name "


first = form_validation()

print(first)
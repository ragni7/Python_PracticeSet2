import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def CheckEmail():
	email = input("Please enter email:", )
	if(re.fullmatch(regex, email)):
		print("Valid Email")

	else:
		print("Invalid Email")

x = CheckEmail()
print(x)


def Authentication():
    Login = {'username1':'password1', 'username2':'password2'}
    username = input("Username is=", )
    password = input("Password is=", )
    if username in Login and Login[username] == password:
        print("Login successfully")
    else:
        print("Please enter correct Username or Password")
    
x = Authentication()
print(x)
import random

def genratePassword(len):

    list_of_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()" 
    pass_str = " "
    for i in range(len):  
        pass_str = pass_str + random.choice(list_of_chars)
    return pass_str
 
len = 8
pass_str = genratePassword(len)   
print("A randomly generated Password is:", pass_str)  
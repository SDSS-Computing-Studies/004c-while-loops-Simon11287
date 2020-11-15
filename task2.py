#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied
"""
name = ""
password = ""
username=(input("Enter username")).strip()
password=(input("Enter password")).strip()
while username !="admin" or password !=("12345"):
    print("access denied")
    username=(input("Enter username")).strip()
    password=(input("Enter password")).strip()
if username =="admin" and password==("12345"):
    print("Access granted")

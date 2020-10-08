##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Acces denied
"""

name = ""
password = ""
count = 0

while name != "admin":
    password != "12345"
    name = input("enter your username: ")
    password = input("enter your password: ")
    if name != "admin":
        print("  Access denied")
        count = count + 1
        if count > 2:
         break
    elif password != "12345":
        
        if password != "12345":
         print("access deinied")
        else  :
          print("Access granted")

print("Access denied")

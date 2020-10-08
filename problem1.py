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

import math


name = ""
password = ""

while name != "Admin":

    name = input("enter your username: ")
    if name != "Admin":
        print("  Access denied")
        count = 0
        count = count + 1
        if count > 2:
         break
    else :
        print("Access granted")
    
while password != "12345" :
    password = input("enter your password: ")
    if password != "12345":
     print("  Access denied")
    else :
     print("Access granted")

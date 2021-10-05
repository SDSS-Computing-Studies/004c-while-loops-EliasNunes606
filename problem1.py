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
Access denied

example:
example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 1234
Access denied
Too many failed attempts. Access denied.


while <condition>:          # condition is the conditional statement when you want the program to keep going
    commands


while True:
    commands
    if <condition>:         #condtion when you want to break out
        break
"""
counter = 0
while True:
    username = str(input("Enter username: ")).strip()
    password = str(input("Enter password: ")).strip()
    if username != "admin" and password != "12345":
        print("Access denied")
        counter = counter + 1
        if counter == 3:
            print("Too many failed attempts. Access denied.")
            exit()
    else:
        break

print("Access granted")
    

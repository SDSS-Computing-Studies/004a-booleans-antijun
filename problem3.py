#! python3

#  Have the user enter a username 
# If the username is not "admin" then tell them it is an "invalid user", 
# but if it is, then ask them for a password 
# If they get the password correct (password is 12345password) 
# then display the message "Access granted"
# 1 marks

username = input("Enter a username: ")
admin = "admin"
correct_password = "12345password"

if username == admin:
    password = input("Enter your password: ")
    if password == correct_password:
        print("Access granted")
    else:
        print("invalid user")
else:
    print("invalid user")






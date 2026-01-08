
#h WAP program to log in into instagram by entering correct username and password.

user = 'mal'
pwd = 'mal@123'

username = input('Enter your username:')
password = input('Enter your password:')
if username == user:
    if password == pwd:
        print('Login Successful...')
    else:
        print('Incorrect Password...')  
else:
    print('Username not found...')

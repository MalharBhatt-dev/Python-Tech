
class Login :
    def login(self) :
        while True:
            username = input ('Enter the Username :')
            if self.USERNAME == username:
                password = input('Enter the password :')
                if self.PASSWORD == password:
                    print('Login Successful!')
                    break
                else:
                    print('Password is incorrect.')
            else : 
                print('Username is incorrect.')

#hcreate a class login , class add followers , class instagram which inherits from class login and add followers .

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
        
class Followers :
    def add_followers(self):
        self.FOLLOWERS += 1
        print('Follower Added',self.FOLLOWERS)


    def remove_followers(self):
        if self.FOLLOWERS > 0:
            self.FOLLOWERS -= 1
            print('Follower Removed',self.FOLLOWERS)
        else :
            print('No Followers to remove')

class Instagram(Followers , Login):
    founded_year = 2010
    ceo = 'Mr. Malhar'

    def __init__ (self , username , password , followers , following ,noofpost):
        self.USERNAME = username 
        self.PASSWORD = password
        self.FOLLOWERS = followers
        self.FOLLOWING =following
        self.NO_POST = noofpost

a1 = Instagram('mal','mal@12',10,12,20)
a2 = Instagram('sal' , 'sal@12' , 12,10,23)


a1.login()
a1.add_followers()
a1.remove_followers()

a2.login()
a2.add_followers()
a2.remove_followers()

    
    
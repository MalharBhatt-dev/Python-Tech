from class1 import *
from class2 import *
#h from fname import */functname/cname

#! from filename import * ---> ALL THE THINGS WILL GET IMPORTED FROM THE FILE
#! from filename import fname ---> ONLY PARTICULAR FUNCTION WILL GET IMPORTED
#! from filename import cname ---> ONLY PARTICULAR CLASS WILL GET IMPORTED

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
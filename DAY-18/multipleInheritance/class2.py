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
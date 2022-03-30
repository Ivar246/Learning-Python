class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0 
        
    def follow(self, user):
        user.followers +=1
        self.following += 1
         

user_1 = User('001', 'ravi')
user_2 = User('002', 'john')

user_1.follow(user_2) 
"""
user1 objects ko lagi follower method maa user2 objects as parameter jane vayo ani 
user2.followers +=1 matlab user 2 ko follower 1 hune vayo..
"""


print('User_1:')
print(f'follower: {user_1.followers}')
print(f'following: {user_1.following}')
print('\nUser_2')
print(f'follower: {user_2.followers}')
print(f'following: {user_2.following}')
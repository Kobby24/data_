class User:
    def __init__(self, userid, username):
        self.id = userid
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


User1 = User("001", "Gilbert")


User2 = User("002", "Anasiata")
print(User2.username)
print(User2.id)
User2.follow(User1)
print(User2.following)
print(User2.followers)
print(User1.following)
print(User1.followers)
class User:
    def __init__(self, user_id, username):
        print("new user is being created")
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001","Bono")
user_2 = User("002","Juno")

print(user_1.user_id)
print(user_1.username)
print(user_2.followers)
print(user_1.following)
user_1.follow(user_2)
print(user_1.following)
print(user_2.followers)


class Car:
    def __init__(self,seats):
        self.seats = seats
    def enter_race_mode(self):
        self.seats = 2
car_1 = Car(5)

#use displayInfo()
#ride()
#reverse

class User:

    def __init__(self, name, price, max_speed, miles):
        #instance attributes
        self.name = name
        self.price = price
        self.max_speed = max_speed
        self.miles = miles

    def displayInfo(self):
        return self.price

    def get_speed(self):
        return self.max_speed

    def show_mile(self):
        return self.miles
    
    def increase_speed(self):
        print("increasing speed")
        return 0

    def increase_speed(self):
        print("increasing speed")
        return 0

# User()
user1 = User("Lance Armstrong", "400", "40mph", "450miles")
user2 = User("Mia", "300", "45mph", "300miles")

# user2.miles = "500"
# user1.name = "Ninja"


print(user2.show_mile())
print(user1.name)



#chainingmethod user1.login().show().logout()
# user1.self().name().price().max_speed().miles()
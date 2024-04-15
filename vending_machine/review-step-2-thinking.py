class VendingMachine:
    # initialize money_list, Define the variables
    def __init__(self):
        self.money_list = []
        self.not_allowed_money = [1, 5, 2000, 5000, 10000]  # step 1

    def insert_money(self, money):
        if money in self.not_allowed_money:  # step 1
            return  # step 1
        self.money_list.append(money)

    def refund(self):
        result = sum(self.money_list)
        return result

class DrinkManager:
    def __init__(self):
        self.drink_list = []

    def get_drink_list(self):
        return self.drink_list

    def set_drink(self, drink):
        self.drink_list.append(drink)

    def get_drink_price(self, drink_name):
        price = 0
        for drink in self.drink_list:
            if drink["name"] == drink_name:
                price = drink["price"]
        return price

    def get_drink_name(self, drink_price):
        drink_name_list = []
        for drink in self.drink_list:

            # if the drink is in drink_name_list, skip the logic
            if drink["name"] in  drink_name_list:
                continue
            if drink["price"] == drink_price:
                drink_name_list.append(drink["name"])
        return drink_name_list


d = DrinkManager()
drink_list = d.get_drink_list()

# Add 5 bottles of coke
for i in range(5):
    d.set_drink({"name": "coke", "price": 120})

# total logic
total = 0
for i in drink_list:
    total += 1
print(f"The total is {total}.")

# price
drink_price = d.get_drink_price("coke")
print(f"The price is {drink_price}.")

# name
drink_name = d.get_drink_name(120)
print(f"The name is {drink_name}")

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


class VendingMachine:
    # initialize money_list, Define the variables
    def __init__(self):
        self.money_list = []
        self.not_allowed_money = [1, 5, 2000, 5000, 10000]  # step 1
        self.d = DrinkManager()
        self.drink_list = self.d.get_drink_list()
        print(self.drink_list)


    def insert_money(self, money):
        if money in self.not_allowed_money:  # step 1
            return  # step 1
        self.money_list.append(money)

    def refund(self):
        result = sum(self.money_list)
        return result

    def set_drink(self, drink):
        d = DrinkManager()
        d.set_drink(drink)
        # print(drink)

    def get_drink_name(self, drink_price):
        d = DrinkManager()
        print(f"drink_list is {d.get_drink_list()}だに")
        result = d.get_drink_name(drink_price)
        return result

    def get_drink_price(self, drink_name):
        d = DrinkManager()
        result = d.get_drink_price(drink_name)
        return result

    def get_stock(self):
        d = DrinkManager()
        drink_list = d.get_drink_list()
        # total logic
        print(drink_list)
        total = 0
        for i in drink_list:
            total += 1
        print(f"The total is {total}.")
        return total
    def get_drink_list(self):
        result = self.d.get_drink_list()
        return result 




v = VendingMachine()
v.insert_money(1000)
v.insert_money(1)
v.insert_money(1000)
v.insert_money(1)
result_refund = v.refund()

print(f"お釣りは{result_refund}だに。")
d = DrinkManager()

# Set drink
# Add 5 bottles of coke
for i in range(5):
    d.set_drink({"name": "coke", "price": 120})
# This is Ok
print(d.get_drink_list())

print(v.get_drink_list())

# Get drink name
print(v.get_drink_name(120))
print(v.get_drink_price("coke"))
drink_price = v.get_drink_price("coke")
print(drink_price)

# Get drink price
print(v.get_drink_price("coke"))

# Get total of stocks
print(f"The total2 is {v.get_stock()}")
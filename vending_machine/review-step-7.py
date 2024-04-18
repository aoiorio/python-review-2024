import random

def get_unique_list(drink_list):
    seen = []
    return [x for x in drink_list if x not in seen and not seen.append(x)]

class VendingMachine:
    # initialize money_list, Define the variables
    def __init__(self):
        self.money_list = []
        self.not_allowed_money = [1, 5, 2000, 5000, 10000]  # step 1
        self.profits = 0
        self.refund_money = 0
        self.drinks_you_can_buy = []

    def insert_money(self, money):
        if money in self.not_allowed_money:  # step 1
            return  # step 1
        self.money_list.append(money)

    def get_change(self):
        result = sum(self.money_list)
        return result

    # It can effect any drinks!
    def buy_drink(self, drink_list, drink_name):
        can_buy_drink = False
        # I want to use refund method, but I couldn't
        money = sum(self.money_list)

        # check money and stock are enough for buying coke
        for drink in drink_list:
            if drink["name"] == drink_name and money >= drink["price"]:
                can_buy_drink = True
                print(f"You can buy a {drink_name}!! Because it's {can_buy_drink}!")

                # buy a drink
                drink_list.remove(drink)
                # Add to profits
                self.profits += drink["price"]

                # Calculate refund_money
                self.refund_money = money - drink["price"]
                print(f"You bought a {drink_name}!")

                # Get your change
                print(f"Your change is {self.refund_money}")
                c = Change()
                print(f"Specifically, Your change is {c.get_change(self.refund_money)}")
                print(f"The stock of change is now {c.change_money_dict}")

                return

        # if the user don't have enough money or there's no stock in this vending machine
        print(f"Sorry, you can't buy a {drink_name} now, because it's {can_buy_drink}")

    def get_drinks_you_can_buy(self, drink_list):
        money = sum(self.money_list)
        result = []
        # これは、ドリンクがあるものだから。確認しなくても大丈夫
        for drink in drink_list:
            if money >= drink["price"] and not drink in self.drinks_you_can_buy:
                self.drinks_you_can_buy.append(drink)

        return self.drinks_you_can_buy

    def buy_random_drink(self, drink_list,):
        random_drink_list = [{"name": "coke", "price": 120}, {"name": "dietcoke", "price": 120}, {"name": "tea", "price": 120}]
        new_random_drink_list = []
        unique_drink_list = get_unique_list(drink_list)

        for unique_drink in unique_drink_list:
            if unique_drink in random_drink_list:
                new_random_drink_list.append(unique_drink)
        if not new_random_drink_list:
            print(f"Sorry, you can't buy a random drink now, because the stock is empty now.")
            return

        # buy a random drink from random_drink_list
        random_drink_index_for_buying = random.randrange(len(new_random_drink_list))
        v.buy_drink(drink_list, random_drink_list[random_drink_index_for_buying]["name"])


        # TODO from this, I think I should separate logic no I don't need it.
        """
        かぶってもいいのか？？？ 例えば、cokeがdrinks_you_can_buyに入っていたら、randomで取得したcokeを入れてもいいのか？？
        いいことにしよう！！
        # random_drink_index = random.randrange(len(drinks_you_can_buy))

        # If there's same one in random_drink_list reassign the value
        # while drinks_you_can_buy[random_drink_index] in random_drink_list:
        #     random_drink_index = random.randrange(len(drinks_you_can_buy))

        # new_random_drink_list.append(drinks_you_can_buy[random_drink_index])

        # self.drinks_you_can_buy.append(drinks_you_can_buy[random_drink_index])
        # print("wtf")
        # print(new_random_drink_list)
        # return self.drinks_you_can_buy
        """

        self.drinks_you_can_buy.append({"name": random_drink_list[random_drink_index_for_buying]["name"], "price": self.refund_money})
        print(f"For now, you can buy ☟☟☟☟☟☟\n{self.drinks_you_can_buy}")

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
            if drink["name"] in drink_name_list:
                continue
            if drink["price"] == drink_price:
                drink_name_list.append(drink["name"])
        return drink_name_list



class Change:
    def __init__(self) -> None:
        self.change_money_dict = {
            "1000": 10,
            "500": 10,
            "100": 10,
            "50": 10,
            "10": 10,
        }

    # PLEASE plus the value into change_money with insert_money
    def get_change(self, change_money):
        separate_change_money_dict = {"1000": 0, "500": 0, "100": 0, "50": 0, "10": 0}
        str_change_money = str(change_money)
        """
        1. お釣りのお金(change_money)を1000円札、500円、100円、50円、10円に分割する
        I hope the type will be dictionary (e.g. 1010円の場合, {1000: 1, 500: 0, 100: 0, 50: 0, 10: 1}となる)
        2. 位の数を調べれば大丈夫！！ (e.g. 1010円だったら、桁数を調べて、この場合4桁だから4桁目1があり1000円が一枚、2の位に1があるから10円が一枚)
        分ける数字は反対からやれば数字が尽きるからいいかも
        3. 50円は、100円以下(100 > xね)だった場合に、50で割れるかを計算する。
        """

        change_money_list = list(str_change_money)
        # Reverse the order of change_money_list
        change_money_list.reverse()
        for i in range(1, len(change_money_list)):
            key = "1" + "0" * i

            # Calculate 50 Yen
            if key == '10' and int(change_money_list[i]) >= 5:
                separate_change_money_dict['50'] = "1"

                # Summarize 10 Yen
                if int(change_money_list[i]) - 5 >= 0:
                    current_value = separate_change_money_dict["10"]
                    separate_change_money_dict["10"] = current_value + int(change_money_list[i]) - 5
                continue

            # Calculate 100 Yen
            if key == '100' and int(change_money_list[i]) >= 5:
                separate_change_money_dict['500'] = "1"

                # Summarize 100 Yen
                if int(change_money_list[i]) - 5 >= 0:
                    current_value = separate_change_money_dict["100"]
                    separate_change_money_dict["100"] = current_value + int(change_money_list[i]) - 5
                continue


            separate_change_money_dict[key] = change_money_list[i] # Set the value that I got

        self.change_money_dict["1000"] = self.change_money_dict["1000"] - int(separate_change_money_dict["1000"])
        self.change_money_dict["500"] = self.change_money_dict["500"] - int(separate_change_money_dict["500"])
        self.change_money_dict["100"] = self.change_money_dict["100"] - int(separate_change_money_dict["100"])
        self.change_money_dict["50"] = self.change_money_dict["50"] - int(separate_change_money_dict["50"])
        self.change_money_dict["10"] = self.change_money_dict["10"] - int(separate_change_money_dict["10"])

        # If the change is not enough, return "0"
        if "10000" in separate_change_money_dict.keys():
            return "0"

        return separate_change_money_dict



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

print("-------------------------------------------")
v = VendingMachine()
v.insert_money(200)

# Buy drink
v.buy_drink(drink_list, "coke")
# v.get_stock()

print('-------------------------------------------')
# Get profits
print(f"The profits of Atom's vending machine are {v.profits}")

# Get refund (this is redundant because there's print(change))
print(f"Your refund money is {v.refund_money}")

# Add 5 bottles of redbull
for i in range(5):
    d.set_drink({"name": "redbull", "price": 200})

# Add 5 bottles of water
for i in range(5):
    d.set_drink({"name": "water", "price": 100})

# Get drinks that you can buy with your money
drinks_you_can_buy = v.get_drinks_you_can_buy(drink_list)
print(f"You can buy {drinks_you_can_buy}")

print('-------------------------------------------')
# Add 5 bottles of dietcoke
for i in range(5):
    d.set_drink({"name": "dietcoke", "price": 120})

# Add 5 bottles of tea
for i in range(5):
    d.set_drink({"name": "tea", "price": 120})

# reassign or update drinks_you_can_buy
drinks_you_can_buy = v.get_drinks_you_can_buy(drink_list)

v.buy_random_drink(drink_list)
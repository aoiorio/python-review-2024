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

v = VendingMachine()

# insert money
v.insert_money(1000)
v.insert_money(1)
v.insert_money(1000)
v.insert_money(1)
result_refund = v.refund()

print(f"お釣りは{result_refund}だに。")

class Customer:
    def __init__(self, name, wallet, ages ,drunk_level):
        self.name = name
        self.wallet = wallet
        self.age = ages
        self.drunk_level = drunk_level

    def buy_drink(self, amount):
        self.wallet -= amount

    def increase_drunkness(self):
        self.drunk_level += 1
    
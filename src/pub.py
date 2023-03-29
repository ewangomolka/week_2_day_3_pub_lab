
class Pub:
    def __init__(self, name, till, minimum_age, drunk_level):
        self.name = name
        self.till = till
        self.minimum_age = minimum_age
        self.drunk_level = drunk_level

    

    def increase_till(self, amount):
        self.till += amount

    def check_age(self, customer):
        return customer.age >= 18
    
    def check_drunkness(self, customer):
        if customer.drunk_level > 5:
            return False
        else:
            return True

    def serve_customer(self, customer):
        if self.check_drunkness(customer) == False:
            return "Too Drunk"
        else:
            return "What can i get you?"

                

    
    # 3 A's of testing [1. Arrange, 2. Act, 3. Assert]
import unittest
from src.pub import Pub
from src.drinks import Drinks
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00, 18, 5)
        self.drinks = Drinks("Beer", 5.50, 1)
        self.customer = Customer("Gandalf", 80.00, 50 , 6)
        self.customer2 = Customer("Sam", 20.00, 17 , 2)
        


    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_increase_till(self):
        self.pub.increase_till(2.50)
        # expected = 102.50
        # actual = self.pub.till
        # self.assertEqual(expected, actual)
        self.assertEqual(102.50, self.pub.till)

    def test_can_customer_buy_drink(self):
        self.customer.buy_drink(5.50)
        self.pub.increase_till(5.50)

        self.assertEqual(74.50, self.customer.wallet)

    def test_is_customer_old_enough(self):
        check_age_result = self.pub.check_age(self.customer2)
        self.assertEqual(False, check_age_result)
    
    def test_is_customer_old_enough_yes(self):
        check_age_result = self.pub.check_age(self.customer)
        self.assertEqual(True, check_age_result)

    def test_drunkeness_not_drunk(self):
        check_drunkeness_result = self.pub.check_drunkness(self.customer2)
        self.assertEqual(True, check_drunkeness_result)

    def test_drunkeness_is_drunk(self):
        check_drunkeness_result = self.pub.check_drunkness(self.customer)
        self.assertEqual(False, check_drunkeness_result)

    def test_drink_makes_customer_drunk(self):
        self.customer.increase_drunkness()
        self.assertEqual(7, self.customer.drunk_level)

    def test_refuse_service(self):
        serving_result = self.pub.serve_customer(self.customer)
        self.assertEqual("Too Drunk", serving_result)
        # print(self.customer.drunk_level)
    def test_allow_service(self):
        serving_result = self.pub.serve_customer(self.customer2)
        self.assertEqual("What can i get you?", serving_result)


        
    

    
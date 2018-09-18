

# Farmers_Market.py
# Author: Jason Greve
# Client: ObjectRocket
# Created: 2018-SEP-17-MON
# Updated: 
# Description: see gistfile1.txt

import unittest
from Register import Register
from Products_2018 import products_2018 as products
from Anniversary_Specials_2018 import AnniversarySpecials2018
from Anniversary_Promo_2018 import anniversary_promo_2018 as specials



class TestPurchases(unittest.TestCase):
 
    def setUp(self):
        self.register = Register(products, specials)
    
    def test_objectrocket(self):
        print('\nCommencing ObjectRocket Tests')
        self.assertAlmostEqual(self.register.test(['CH1', 'AP1', 'CF1', 'MK1']), 20.34)
        self.assertAlmostEqual(self.register.test(['MK1', 'AP1']), 10.75)
        self.assertAlmostEqual(self.register.test(['CF1', 'CF1']), 11.23)
        self.assertAlmostEqual(self.register.test(['AP1', 'AP1', 'CH1', 'AP1']), 16.61)
        print('Completed ObjectRocket Tests')
        
    def test_jasongreve(self):
        print('Commencing JasonGreve Tests')
        self.assertAlmostEqual(self.register.test(['CH1', 'CF1', 'AP1', 'AP1', 'CH1', 'CF1', 'MK1', 'MK1']), 34.20)
        self.assertAlmostEqual(self.register.test(['CF1', 'MK1', 'MK1', 'CH1', 'CF1', 'CF1']), 30.32)
        self.assertAlmostEqual(self.register.test(['AP1', 'OM1', 'OM1']), 10.38)
        self.assertAlmostEqual(self.register.test(['AP1', 'AP1', 'OM1', 'OM1']), 13.38)
        self.assertAlmostEqual(self.register.test(['AP1', 'AP1', 'OM1', 'OM1', 'AP1']), 14.88)
        self.assertAlmostEqual(self.register.test(['AP1', 'AP1', 'OM1', 'OM1', 'AP1', 'OM1']), 15.57)
        self.assertAlmostEqual(self.register.test(['AP1', 'AP1', 'OM1', 'OM1', 'AP1', 'OM1', 'AP1']), 20.07)
        self.assertAlmostEqual(self.register.test(['OM1', 'AP1', 'AP1', 'OM1', 'OM1', 'AP1', 'OM1', 'AP1']), 20.76)
        self.assertAlmostEqual(self.register.test(['CH1', 'AP1', 'CF1', 'CF1', 'MK1', 'OM1', 'CF1', 'CH1', 'MK1']), 40.12)
        print('Completed JasonGreve Tests')


def interactive_testing():
    cart = []
    discounts = []
    register = Register(products, specials)
    flag = True
    while(flag):
        prod = input('Enter a product code to add to the basket:\n'+
                     "Type 'CH1' for 'Chai'\n"+
                     "Type 'AP1' for 'Apples'\n"+
                     "Type 'CF1' for 'Coffee'\n"+
                     "Type 'MK1' for 'Milk'\n"+
                     "Type 'OM1' for 'Oatmeal'\n"+
                     "Type 'exit' or 'quit' to end your session.\n"+
                     ">>> ")
        
        if prod.lower() == 'exit' or prod.lower() == 'quit':
            flag = False
            break
        if prod not in register.products.keys():
            print("Sorry, not a valid product ID. Try again.")
            continue
        
        register.purchase(prod)
        register.print_basket()

def testing_menu():
    choice = ''
    while(choice not in ('1','2')):
        choice = input("Type '1' to run unit tests.\n"+
                       "Type '2' to add items to the register/basket.\n>>> ")
        if choice == '1':
            unittest.main()
        if choice == '2':
            interactive_testing()
            break




if __name__ == '__main__':
    testing_menu()










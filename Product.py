
# Product.py
# Author: Jason Greve
# Client: ObjectRocket
# Created: 2018-SEP-17-MON
# Updated:
# Description: Base class for modelling Farmer's Market products.

from Specials import Specials

class Product(object):
    
    def __init__(self, prod_code, name, price):
        self.prod_code = prod_code # product code: CH1, AP1, etc.
        self.name = name # Chai, Apples, etc.
        self.price = price # float
        self.discounts = [] # a list of dicts containing 3 K/V pairs
        self.total = self.price # float
    
    def calc_total(self):
        self.total = self.price
        for d in self.discounts:
            # d['func'] is a function reference
            self.total = d['func'](self.total, d['amt'])

    def print_product(self):
        # prints the 3 character product code, and the regular product price
        print('{0:<18}{1:>17.2f}'.format(self.prod_code, self.price))
        for d in self.discounts:
            # prints the 4 letter promo code, and the amount of the discount
            if d['func'] == Specials.difference:
                print(' '*12+'{0:<11}{1:>12.2f}'.format(d['disc'], -1.0*d['amt']))
            if d['func'] == Specials.multiply:
                print(' '*12+'{0:<11}{1:>12.2f}'.format(d['disc'], -1.0*d['amt']*self.price))







# Register.py
# Author: Jason Greve
# Client: ObjectRocket
# Created: 2018-SEP-17-MON
# Updated: 
# Description: Partial model of a simple cash register.

from Product import Product


class Register(object):
    
    def __init__(self, products, specials):
        # ex. {'CH1':{'name':'Chai','price':3.11}, ...}
        self.products = products
        # OrderedDict, ex. {'BOGO':AnniversarySpecials2018.bogo, ...}
        self.specials = specials
        self.basket_state = [] # list of Product objects
        
    def purchase(self, prod_code):
        self.basket_state.append(Product(prod_code,
                                         self.products[prod_code]['name'],
                                         self.products[prod_code]['price']))
        self.apply_discounts() # populate Product with discount data
    
    def add_items(self, items):
        for item in items:
            self.purchase(item)
    
    def print_basket(self):
        print('{0:<18}{1:>17}'.format('Item', 'Price'))
        print('{0:<18}{1:>17}'.format('-'*4, '-'*5))
        for item in self.basket_state:
            item.print_product()
        print('-'*35)
        print('{:>35.2f}'.format(self.calc_total()))
    
    def apply_discounts(self):
        for item in self.basket_state:
            item.discounts = [] # don't apply the same discount more than once!
        for key, function in self.specials.items():
            # the function (ex. 'bogo') gets applied to all appropriate items
            # in basket_state
            function(self.basket_state)
    
    def calc_total(self):
        total = 0
        for item in self.basket_state:
            item.calc_total()
            total += item.total
        return total

    def test(self, basket):
        '''unittest helper method'''
        self.add_items(basket)
        total = self.calc_total()
        # clear basket for next batch of products
        self.basket_state = []
        return total



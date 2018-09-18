
# Specials.py
# Author: Jason Greve
# Client: ObjectRocket
# Created: 2018-SEP-17-MON
# Updated:
# Description: Base class for modelling promotional specials.


class Specials(object):
    
    # the arithmetic operations are written as 2 argument functions
    # the logic which applies them could apply any 2 arg function 
    # of arbitrary complexity
    @classmethod
    def difference(self, minuend, subtrahend):
        return minuend - subtrahend
    
    @classmethod
    def multiply(self, multiplier, multiplicand):
        return multiplier * multiplicand
    
    @classmethod
    def count_items(self, basket, prod_code):
        '''product code raw-frequency'''
        counter = 0
        for item in basket:
            if item.prod_code == prod_code:
                counter += 1
        return counter
    











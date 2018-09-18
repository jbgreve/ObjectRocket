
# Anniversary_Specials_2018.py
# Author: Jason Greve
# Client: ObjectRocket
# Created: 2018-SEP-17-MON
# Updated:
# Description: Child class of Specials; models 2018 Farmer's Market 
#              Anniversary specials business rules.


from Specials import Specials

class AnniversarySpecials2018(Specials):
    
    @classmethod
    def bogo(self, basket):
        '''BOGO -- Buy-One-Get-One-Free Special on Coffee. (Unlimited)'''
        counter = 0
        for item in basket:
            if item.prod_code == 'CF1':
                counter += 1
                # only even numbered (every other) packages of 
                # coffee get the BOGO promo
                if counter % 2 == 0:
                    item.discounts.append({'disc' : 'BOGO', 
                                           'func' : Specials.difference, 
                                           'amt'  : item.price})
    
    @classmethod
    def appl(self, basket):
        '''APPL -- If you buy 3 or more bags of Apples, the price drops to $4.50.'''
        # ensure there are at least 3 bags of apples
        if Specials.count_items(basket, 'AP1') >= 3:
            for item in basket:
                if item.prod_code == 'AP1':
                    item.discounts.append({'disc' : 'APPL', 
                                           'func' : Specials.difference, 
                                           'amt'  : 1.50})
    
    @classmethod
    def chmk(self, basket):
        '''CHMK -- Purchase a box of Chai and get milk free. (Limit 1)'''
        # ensure there is at least one box of chai and one carton of milk
        if Specials.count_items(basket, 'CH1') >= 1 and Specials.count_items(basket, 'MK1') >= 1:
            for item in basket:
                if item.prod_code == 'MK1':
                    item.discounts.append({'disc' : 'CHMK', 
                                           'func' : Specials.difference, 
                                           'amt'  : item.price})
                    break
    
    @classmethod
    def calc_apom_bags(self, basket):
        '''calculates many bags of apples get discounted'''
        oatmeal = Specials.count_items(basket, 'OM1')
        apples = Specials.count_items(basket, 'AP1')
        if oatmeal >= apples:
            return apples
        return oatmeal
    
    @classmethod
    def apom(self, basket):
        '''APOM -- Purchase a bag of Oatmeal and get 50% off a bag of Apples'''
        bags = self.calc_apom_bags(basket)
        for item in basket:
            if item.prod_code == 'AP1' and bags > 0:
                item.discounts.append({'disc' : 'APOM', 
                                       'func' : Specials.multiply, 
                                       'amt'  : 0.5})
                bags -= 1





# Anniversary_Promo_2018.py
# Author: Jason Greve
# Client: ObjectRocket
# Created: 2018-SEP-17-MON
# Updated:
# Description: Data for Farmers_Market.py (Register Class)


from collections import OrderedDict
from Anniversary_Specials_2018 import AnniversarySpecials2018 as AnSpec

# OrderedDict ensures that APOM will be applied before APPL.
# This ensures that the customer will get the largest discount
# when buying 3 or more bags of apples and one or more bags of 
# oatmeal. (The rules interact and are not commutative)

# The following example shows different ways to calculate the 
# price for a bag of apples when both APOM and APPL apply:
# (6 * 0.5) * 0.75 = 2.25   APOM >> APPL "ratio" discount
# (6 * 0.75) * 0.5 = 2.25   APPL >> APOM "ratio" discount
# (6 * 0.5) - 1.25 = 1.75   APOM >> APPL "fixed" discount <<--- Best Price for Customer
# (6 - 1.25) * 0.5 = 2.375  APPL >> APOM "fixed" discount

anniversary_promo_2018 = OrderedDict()
anniversary_promo_2018['BOGO'] = AnSpec.bogo
anniversary_promo_2018['CHMK'] = AnSpec.chmk
anniversary_promo_2018['APOM'] = AnSpec.apom
anniversary_promo_2018['APPL'] = AnSpec.appl




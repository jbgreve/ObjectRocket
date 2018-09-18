FROM python:3

ADD Farmers_Market.py /
ADD Register.py /
ADD Anniversary_Specials_2018.py /
ADD Anniversary_Promo_2018.py /
ADD Product.py /
ADD Products_2018.py /
ADD Specials.py /

CMD [ "python", "./Farmers_Market.py" ]

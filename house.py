#-*- coding: UTF-8 -*-

import io  
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')

from lib.requests import Request
from bs4 import BeautifulSoup

city = "beijing"
domain = "anjuke.com"

house_id = "A1203790492"

class House:
    protocol = 'https'
    domain = 'anjuke.com'

    def __init__(self, city, house_id):
        self.city = city
        self.house_id = house_id
        self.get_data()
    
    def get_url(self):
        return "%s://%s.%s/prop/view/%s" % (House.protocol, self.city, House.domain, self.house_id)

    def get_data(self):
        content = Request.do(self.get_url())
        self.data = BeautifulSoup(content, "html.parser")
        return self.data

    def get_title(self):
        return self.data.find(id="container").h3.get_text().strip()

    def get_price(self):
        price_str = self.data[0].select('#content > div.wrapper')[0].select('div.wrapper-lf.clearfix')[0].select('div.basic-info.clearfix')[0].select('span.light.info-tag')[0].em.text
        return float(price_str) * 10000

    def get_bedroom(self):
        self.data[0].select('#content > div.wrapper')[0].select('div.wrapper-lf.clearfix')[0].select('div.basic-info.clearfix')[0].select('span.info-tag')[0].em[0].text

    def get_livingroom(self):
        self.data[0].select('#content > div.wrapper')[0].select('div.wrapper-lf.clearfix')[0].select('div.basic-info.clearfix')[0].select('span.info-tag')[0].em[1].text

    def get_size(self):
        self.data[0].select('#content > div.wrapper')[0].select('div.wrapper-lf.clearfix')[0].select('div.basic-info.clearfix')[0].select('span.info-tag')[1].em.text

house = House('beijing', 'A1203790492')
print(house.get_title())
print(house.get_price())
print(house.get_size())
print(house.get_bedroom())
print(house.get_liveingroom())

import requests
from bs4 import BeautifulSoup


class GetAllCard:
    def __init__(self, url):
        self.url = url
        self.price_list = []

    def get_all_card_info(self):
        self.get_out_of_stock_card_info()
        self.get_in_stock_card_info()
    
    def get_in_stock_card_info(self):
        class_name = "card-product position-relative mt-4"
        self.get_card_info(class_name)

    def get_out_of_stock_card_info(self):
        class_name = "card-product position-relative mt-4 sold-out"
        self.get_card_info(class_name)

    def get_card_info(self, class_name):
        response = requests.get(url=self.url)
        soup = BeautifulSoup(response.text, 'html5lib')
        cards = soup.find_all('div', class_=class_name)
        for c in cards:
            self.store_card_price(c)

    def store_card_price(self, card_info):
        card_price = {}
        name = card_info.find('h4', class_="text-primary fw-bold").string
        card_price['name'] = name

        price = card_info.find('strong', class_="d-block text-end").string
        price = price.strip()
        card_price['price'] = price
        
        link_object = card_info.find('a')
        link = link_object['href']
        card_price['link'] = link
        
        self.price_list.append(card_price)

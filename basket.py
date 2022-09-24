from product import Catalogue
from shipping import Shipping
from src.offer_service.IOffer import OfferStrategy
from exceptions.pos_exceptions import ProductNotFound

class Basket:

    def __init__(self, catalogue: Catalogue, delivery_type: Shipping, discount_offer: OfferStrategy):
        self.basket_items = {}
        self.catalogue = catalogue
        self.delivery_type = delivery_type
        self.discount_offer_type = discount_offer
        self.total_amount = 0
        self.discount_amount = 0
        self.shipping_charges = 0
        pass

    def add(self, product_code):
        if product_code not in self.catalogue.product_map.keys():
            raise ProductNotFound("Product code chosen is not available in the catalogue, please try again.")
        if product_code in self.basket_items.keys():
            self.basket_items[product_code]['quantity'] += 1
        else:
            self.basket_items[product_code] = {}
            self.basket_items[product_code]['quantity'] = 1
            self.basket_items[product_code]['price'] = self.catalogue.get_catalogue()[product_code].price

        self.update_delivery_charges()
        self.update_offered_discount()

    def update_delivery_charges(self):
        self.shipping_charges = self.delivery_type.get_shipping_charges(self.total_basket_amount())

    def update_offered_discount(self):
        self.discount_amount = self.discount_offer_type.apply_offer(self.basket_items)

    def total_basket_amount(self):
        return sum([self.basket_items[item]['price'] * self.basket_items[item]['quantity'] for item in
                    self.basket_items.keys()])

    def total(self):
        return round((self.total_basket_amount() + self.shipping_charges) - self.discount_amount, 2)

    def show_basket(self):
        return self.basket_items

    def current_status(self):
        return " | Total Cart cost: {} | Current Shipping cost: {} | Discount added : {} |".format(self.total(),
                                                                                        self.shipping_charges,
                                                                                        self.discount_amount)

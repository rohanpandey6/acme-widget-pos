import unittest
from exceptions.pos_exceptions import ProductNotFound
from src.basket import Basket
from product import Catalogue
from shipping import Shipping
from src.offer_service.widget_offer import WidgetOffer


class TestBasket(unittest.TestCase):

    def setUp(self) -> None:
        self.shipping = Shipping()
        self.catalogue = Catalogue()
        self.catalogue.add('A0', 'Test Product A', 2)
        self.catalogue.add('B0', 'Test Product B', 2)
        self.offer_strategy = WidgetOffer('R01')
        self.basket = Basket(self.catalogue, self.shipping, self.offer_strategy)
        self.basket.add('A0')
        self.basket.add('A0')
        self.basket.add('B0')

    def testUnavailableProducts(self):
        self.assertRaises(ProductNotFound, self.basket.add, 'C0')

    def testBasketProductAdd(self):
        self.assertEqual(list(self.basket.show_basket().keys()), ['A0', 'B0'])

    def testTotalBasketAmount(self):
        self.assertEqual(self.basket.total_basket_amount(), 6)

    def testTotal(self):
        self.basket.shipping_charges = 20
        self.basket.discount_amount = 5
        self.assertEqual(self.basket.total(), 21)



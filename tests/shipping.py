import unittest
from src.shipping import Shipping


class TestProduct(unittest.TestCase):

    def setUp(self) -> None:
        self.shipping = Shipping()
        self.test_basket_prices = [100, 65, 23]
        self.expected_shipping = [0, 2.95, 4.95]

    def testFinalShippingCalculation(self):
        calculated_prices = []
        for prices in self.test_basket_prices:
            calculated_prices.append(self.shipping.get_shipping_charges(prices))

        self.assertEqual(calculated_prices, self.expected_shipping)

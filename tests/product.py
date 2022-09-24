import unittest
from exceptions.pos_exceptions import ProductAlreadyExists
from src.product import Catalogue


class TestProduct(unittest.TestCase):

    def setUp(self) -> None:
        self.catalogue = Catalogue()
        self.catalogue.add('A0', 'Test Product A', 2)
        self.catalogue.add('B0', 'Test Product B', 2)

    def testDuplicateProducts(self):
        self.assertRaises(ProductAlreadyExists, self.catalogue.add, 'A0', 'Product Duplicate A', 2)

    def testCatalogueProductAdd(self):
        self.assertEqual(list(self.catalogue.get_catalogue().keys()), ['A0', 'B0'])

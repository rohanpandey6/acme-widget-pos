from exceptions.pos_exceptions import ProductAlreadyExists


class Product:
    def __init__(self, product_code: str, product_name: str, price: float):
        self.product_code = product_code
        self.product_name = product_name
        self.price = price

    def __repr__(self):
        return '{}:{}:{}'.format(self.product_code, self.product_name, self.price)


class Catalogue:
    def __init__(self):
        self.product_map = {}

    def add(self, product_code, product_name, product_price):
        if product_code in self.product_map.keys():
            raise ProductAlreadyExists("Product with code: {} already exists".format(product_code))
        self.product_map[product_code] = Product(product_code, product_name, product_price)

    def get_catalogue(self):
        return self.product_map

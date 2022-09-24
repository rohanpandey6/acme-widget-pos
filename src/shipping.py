class Shipping:
    @staticmethod
    def get_shipping_charges(current_basket_price):
        if current_basket_price > 90:
            return 0
        if current_basket_price > 50:
            return 2.95
        else:
            return 4.95

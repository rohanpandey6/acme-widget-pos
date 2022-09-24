import sys
from product import Catalogue
from tabulate import tabulate
from shipping import Shipping
from basket import Basket
from src.offer_service.widget_offer import WidgetOffer
from exceptions.pos_exceptions import ProductNotFound

present_catalogue = Catalogue()
present_delivery_charges = Shipping()
present_offer = WidgetOffer

present_catalogue.add('R01', 'Red Widget', 32.95)
present_catalogue.add('G01', 'Green Widget', 24.95)
present_catalogue.add('B01', 'Blue Widget', 7.95)

rows = []
for product in present_catalogue.get_catalogue().values():
    rows.append(repr(product).split(':'))

print("\n")
print("*" * 50)
print("Welcome to ACME Widget Co")
print("*" * 50)

print("\n")
print("Product Catalogue")
print("\n")
print(tabulate(rows, headers=['Code', 'Product', 'Price']))
print("\n")
print('*' * 25 + " NOTE " + '*' * 25)
print("Shipping Charges:")
print("For orders under $50: $4.95")
print("For orders more than $50 and under $90: $2.95")
print("Free Delivery for orders more than $90")
print('*' * 56)

print("\n")
print('!' * 25 + " Offers " + '!' * 25)
print("buy one red widget, get the second at half price")
print("\n")

print("\n")
prompt = input("Press Y to start placing order, Q to quit \n>")
print("\n")
if prompt.lower() == 'q':
    print("Thank you for visiting us")
    sys.exit()
if prompt.lower() == 'y':
    print("Initialising your shopping basket...", end='\n\n')
    my_basket = Basket(present_catalogue, present_delivery_charges, WidgetOffer('R01'))
    while True:
        try:
            print("After products are finalised press F to show final invoice", end='\n\n')
            product_code = input("Please enter Code for the product you want to purchase, Or press Q to exit \n>")
            if product_code.lower() == 'q':
                break
            if product_code.lower() == 'f':
                print("Total Amount Owed: $", my_basket.total(), end='\n')
                break
            my_basket.add(product_code)
            print('\n')
            print("Product {} added in your shopping basket".format(product_code), end='\n\n')
            print("Basket: ", my_basket.show_basket(), end='\n\n')
            print("Current Basket Status: ", my_basket.current_status(), end='\n\n')

        except ProductNotFound as err:
            print('\n')
            print(err, end='\n\n')
else:
    print("Incorrect option chosen, please try again later.")
print("Thank you for visiting us!!")

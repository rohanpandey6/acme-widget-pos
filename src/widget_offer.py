from src.offer_service.IOffer import OfferStrategy
from dataclasses import dataclass


@dataclass
class WidgetOffer(OfferStrategy):
    widget_id: str = None

    def apply_offer(self, basket_items):
        if self.widget_id in basket_items.keys():
            discount_amount = 0
            if basket_items[self.widget_id]['quantity'] > 1:
                discounted_items = int(basket_items[self.widget_id]['quantity'] / 2)
                discount_amount += discounted_items * (basket_items[self.widget_id]['price'] / 2)
            return discount_amount
        else:
            return 0

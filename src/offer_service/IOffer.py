from abc import ABC, abstractmethod


class OfferStrategy(ABC):
    @abstractmethod
    def apply_offer(self, basket_items):
        ""

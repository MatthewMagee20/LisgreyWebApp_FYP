from django.test import TestCase
from .models import Basket, BasketItem


# Create your tests here.

class TakeawayTest(TestCase):

    def test_total_less_than_equal_to_zero(self):
        """
        total_less_than_zero() returns true if basket total
        is greater than zero
        """
        total = 00.1
        total_check = Basket(total=total)
        print(total)
        self.assertIs(total_check.total_less_than_zero(), True)

    def test_quantity_less_than_equal_to_zero(self):
        """
        quantity_less_than_zero() returns true if item quantities
        are greater than zero
        """
        quantity = 1
        quantity_check = BasketItem(quantity=quantity)
        self.assertIs(quantity_check.quantity_less_than_zero(), True)

import unittest 
from unittest import TestCase
from price_discount import discount  

class TestDiscount(TestCase):

    def test_list_of_three_prices(self):
        prices = [10, 4, 20]
        expected_discount = 4
        self.assertEqual(expected_discount, discount(prices))

    
    # TODO more unit tests here. Each test should test one scenario
    # example test from lab 
    def test_discount_returns_lowest_price_when_called_with_three_prices(self):
        prices = [15, 8, 22]
        result = discount(prices)
        self.assertEqual(result, 8)
        # test is funciontionally very similar to the one above, just wanted to finish the lab thing


if __name__ == '__main__':
    unittest.main()
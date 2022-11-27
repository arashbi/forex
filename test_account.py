import unittest

import numpy as np

import account as account


class TestStringMethods(unittest.TestCase):

    # def test_short_long(self):
    #     wallet = Wallet()
    #     wallet.trade(0.9, -1)
    #     wallet.trade(0.8, -1)
    #     wallet.trade(0.7, 2)
    #     self.assertEqual(wallet.last_avg_price(), 0)
    #     self.assertEqual(wallet.last_profit(), 0.30)
    #
    # def test_short_3long(self):
    #     wallet = Wallet()
    #     wallet.trade(0.9, -1)
    #     wallet.trade(0.8, -1)
    #     wallet.trade(0.7, 3)
    #     self.assertEqual(wallet.last_profit(), 0.30)
    #
    # def test_short_1long(self):
    #     wallet = Wallet()
    #     wallet.trade(0.9, -1)
    #     wallet.trade(0.8, -1)
    #     wallet.trade(0.7, 1)
    #     self.assertEqual(wallet.last_profit(), 0.15)
    #
    # def test_long_short(self):
    #     wallet = Wallet()
    #     wallet.trade(0.9, 1)
    #     wallet.trade(0.8, 1)
    #     wallet.trade(0.7, -1)
    #     self.assertEqual(wallet.last_avg_price(), 0.85)
    #     self.assertEqual(wallet.last_profit(), -0.15)
    #
    # def test_long_2short(self):
    #     wallet = Wallet()
    #     wallet.trade(0.9, 1)
    #     wallet.trade(0.8, 1)
    #     wallet.trade(0.7, -2)
    #     self.assertEqual(wallet.last_profit(), -0.30)
    #
    # def test_long_short_long(self):
    #     wallet = Wallet()
    #     wallet.trade(0.9, 1)
    #     wallet.trade(0.8, 1)
    #     wallet.trade(0.7, -3)
    #     self.assertEqual(-0.3, wallet.last_profit())
    #     wallet.trade(0.8, 1)
    #     self.assertEqual(-0.40, wallet.last_profit())
    #     wallet.trade(0.8, 1)
    #     wallet.trade(0.7, -2)
    #     self.assertEqual(-0.5, wallet.last_profit())
    #
    # def test_1(self):
    #     wallet = Wallet()
    #     wallet.trade(0.9, 1)
    #     wallet.trade(0.8, 1)
    #     wallet.trade(0.7, -2)
    #     wallet.trade(0.6, -1)
    #     self.assertEqual(0.6, wallet.last_avg_price())
    #     self.assertEqual(-1, wallet.last_position())
    #     self.assertEqual(-0.3, wallet.last_profit())
    #     wallet.trade(0.6, -3)
    #     self.assertEqual(0.6, wallet.last_avg_price())
    #     self.assertEqual(-4, wallet.last_position())
    #     self.assertEqual(-0.3, wallet.last_profit())
    #     wallet.trade(0.7, 3)
    #     self.assertEqual(0.6, wallet.last_avg_price())
    #     self.assertEqual(-1, wallet.last_position())
    #     self.assertEqual(-0.6, wallet.last_profit())
    #
    # def test_2(self):
    #     wallet = Wallet()
    #     wallet.trade(0.9, 1)
    #     wallet.trade(0.8, 1)
    #     wallet.trade(1, -2)
    #     wallet.trade()

    def test_tt(self):
        a = [-1, 2, -3]
        print(account.normalize(a))
if __name__ == '__main__':
    unittest.main()

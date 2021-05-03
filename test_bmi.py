#!/usr/bin/env python3

import unittest

import bmi


class Test(unittest.TestCase):

    def test_weight2kg(self):
    	self.assertEqual(bmi.weight2kg(6,13,12),277);


if __name__ == '__main__':
    unittest.main()

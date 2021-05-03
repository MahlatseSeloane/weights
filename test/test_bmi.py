#!/usr/bin/env python3

import unittest

import bmi


class Test(unittest.TestCase):

    def test_weight2kg(self):
    	self.assertEqual(round(bmi.weight2kg(6,13,12),2),131.36);
    	
    def test_height2metres(self):
    	self.assertEqual(round(bmi.height2metres(5,9),2),1.75);
    	
    def test_categorise(self):
    	self.assertEqual(bmi.categorise(bmi.weight2kg(6,13,12),bmi.height2metres(5,9)), 'B');
    		

if __name__ == '__main__':
    unittest.main()

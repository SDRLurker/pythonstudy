'''
Created on 2016. 1. 24.

@author: donglyeolsin
'''
import unittest
from bowling import Bowling

class Test(unittest.TestCase):

    def setUp(self):
        # given ?
        self.b = Bowling()

    def tearDown(self):
        pass


    def testOneStrike(self):
        # when
        self.b.roll(10)
        # then
        self.assertEqual(['X','','','','','','','','','','','','','','','','','','','',''], self.b.getSymbols())
        self.assertEqual(['','','','','','','','','',''], self.b.getScores())

    def testNormals(self):
        # when
        self.b.roll(10)
        self.b.roll(7)
        self.b.roll(2)
        # then
        self.assertEqual(['X','',7,2,'','','','','','','','','','','','','','','','',''], self.b.getSymbols())
        self.assertEqual([19,28,'','','','','','','',''], self.b.getScores())
        
    def testSpare(self):
        # when
        self.b.roll(10)
        self.b.roll(7)
        self.b.roll(2)
        self.b.roll(7)
        self.b.roll(3)
        #then
        self.assertEqual(['X','',7,2,7,'/','','','','','','','','','','','','','','',''], self.b.getSymbols())
        self.assertEqual([19,28,'','','','','','','',''], self.b.getScores())
        
    def testLastSpare(self):
        # when
        self.b.roll(10)
        self.b.roll(7)
        self.b.roll(2)
        self.b.roll(7)
        self.b.roll(3)
        self.b.roll(9)
        #then
        self.assertEqual(['X','',7,2,7,'/',9,'','','','','','','','','','','','','',''], self.b.getSymbols())
        self.assertEqual([19,28,47,'','','','','','',''], self.b.getScores())

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

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

    # added
    def testTurkey(self):
        # when
        self.b.roll(10)
        self.b.roll(10)
        self.b.roll(10)
        # then
        self.assertEqual(['X','','X','','X','','','','','','','','','','','','','','','',''], self.b.getSymbols())
        self.assertEqual([30,'','','','','','','','',''], self.b.getScores())
        
    def test9Combo(self):
        # when
        self.b.roll(10)
        self.b.roll(10)
        self.b.roll(10)
        self.b.roll(10)
        self.b.roll(10)
        self.b.roll(10)
        self.b.roll(10)
        self.b.roll(10)
        self.b.roll(10)
        # then
        self.assertEqual(['X','','X','','X','','X','','X','','X','','X','','X','','X','','','',''], self.b.getSymbols())
        self.assertEqual([30,60,90,120,150,180,210,'','',''], self.b.getScores())


    # original
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
    #    self.assertEqual([19,28,'','','','','','','',''], self.b.getScores())
        
    def testLastSpare(self):
        # when
        self.b.roll(10)
        self.b.roll(7)
        self.b.roll(2)
        self.b.roll(7)
        self.b.roll(3)
        self.b.roll(9)
        self.b.roll(0)
        #then
        self.assertEqual(['X','',7,2,7,'/',9,'-','','','','','','','','','','','','',''], self.b.getSymbols())
    #    self.assertEqual([19,28,47,'','','','','','',''], self.b.getScores())

    def testFoul(self):
        # when
        self.b.roll(10)
        self.b.roll(7)
        self.b.roll(2)
        self.b.roll(7)
        self.b.roll(3)
        self.b.roll(9)
        self.b.roll(0)
        self.b.roll(8)
        self.b.roll(2)
        self.b.roll(10)
        self.b.roll(7)
        self.b.roll(1)
        self.b.roll(9)
        self.b.roll(0)
        self.b.roll(9)
        self.b.roll('F')
        #then
        self.assertEqual(['X','',7,2,7,'/',9,'-',8,'/','X','',7,1,9,'-',9,'F','','',''], self.b.getSymbols())
    
    def testFinish(self):
        # when
        self.b.roll(10)
        self.b.roll(7)
        self.b.roll(2)
        self.b.roll(7)
        self.b.roll(3)
        self.b.roll(9)
        self.b.roll(0)
        self.b.roll(8)
        self.b.roll(2)
        self.b.roll(10)
        self.b.roll(7)
        self.b.roll(1)
        self.b.roll(9)
        self.b.roll(0)
        self.b.roll(9)
        self.b.roll('F')
        self.b.roll(9)
        self.b.roll(1)
        self.b.roll(9)
        #then
        print self.b.getSymbols()
        self.assertEqual(['X','',7,2,7,'/',9,'-',8,'/','X','',7,1,9,'-',9,'F',9,'/',9], self.b.getSymbols())

        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

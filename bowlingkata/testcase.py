'''
Created on 2016. 1. 23.

@author: donglyeolsin
'''
import unittest

from game import Game

class Test(unittest.TestCase):
    def setUp(self):
        self.g = Game()
    
    def _rollMany(self, n, pins):
        for i in range(n):
            self.g.roll(pins)
    
    def testGutterGame(self):
        self._rollMany(20, 0)
        self.assertEqual(0, self.g.score())
    
    def testAllOnes(self):
        self._rollMany(20, 1)
        self.assertEqual(20, self.g.score())
    
    def _rollSpare(self):
        self.g.roll(5)
        self.g.roll(5) 
    
    def testOneSpare(self):
        self._rollSpare()
        self.g.roll(3)
        self._rollMany(17, 0)
        self.assertEqual(16, self.g.score())
    
    def _rollStrike(self):
        self.g.roll(10)
    
    def testOneStrike(self):
        self._rollStrike()
        self.g.roll(3)
        self.g.roll(4)
        self._rollMany(16,0)
        self.assertEqual(24, self.g.score())
    
    def testPerfectGame(self):
        self._rollMany(12,10)
        self.assertEqual(300, self.g.score())
    
    def testAllFrames(self):
        self._rollMany(18,4)
        self._rollStrike()
        self._rollSpare()
        self.assertEqual(92, self.g.score())

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
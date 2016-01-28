# -*- coding: utf-8 -*-
'''
Created on 2016. 1. 24.

@author: donglyeolsin
'''
import unittest
from bowling import Bowling

class Test(unittest.TestCase):
    def setUp(self):
        # given
        self.b = Bowling()

    def tearDown(self):
        pass

    def _repeatRoll(self, n, pins):
        for i in range(n):
            self.b.roll(pins)
        


    # 문제에서 기본으로 주어진 테스트
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
        self.b.roll(0)
        #then
        self.assertEqual(['X','',7,2,7,'/',9,'-','','','','','','','','','','','','',''], self.b.getSymbols())
        self.assertEqual([19,28,47,56,'','','','','',''], self.b.getScores())

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
        self.assertEqual([19,28,47,56,76,94,102,111,120,''], self.b.getScores())
        
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
        self.assertEqual([19,28,47,56,76,94,102,111,120,139], self.b.getScores())

    # 개인적으로 추가해본 테스트케이스들
    def testTurkey(self):
        # when
        self._repeatRoll(3, 10)
        # then
        self.assertEqual(['X','','X','','X','','','','','','','','','','','','','','','',''], self.b.getSymbols())
        self.assertEqual([30,'','','','','','','','',''], self.b.getScores())
    def test9Combo(self):
        # when
        self._repeatRoll(9, 10)
        # then
        self.assertEqual(['X','','X','','X','','X','','X','','X','','X','','X','','X','','','',''], self.b.getSymbols())
        self.assertEqual([30,60,90,120,150,180,210,'','',''], self.b.getScores())
    def test10Combo(self):
        # when
        self._repeatRoll(10, 10)
        # then
        self.assertEqual(['X','','X','','X','','X','','X','','X','','X','','X','','X','','X','',''], self.b.getSymbols())
        self.assertEqual([30,60,90,120,150,180,210,240,'',''], self.b.getScores())
    def test11Combo(self):
        # when
        self._repeatRoll(11, 10)
        # then
        self.assertEqual(['X','','X','','X','','X','','X','','X','','X','','X','','X','','X','X',''], self.b.getSymbols())
        self.assertEqual([30,60,90,120,150,180,210,240,270,''], self.b.getScores())
    def testPerfectGame(self):
        # when
        self._repeatRoll(12, 10)
        # then
        self.assertEqual(['X','','X','','X','','X','','X','','X','','X','','X','','X','','X','X','X'], self.b.getSymbols())
        self.assertEqual([30,60,90,120,150,180,210,240,270,300], self.b.getScores())
    def testMissOne(self):
        # when
        self._repeatRoll(11, 10)
        self.b.roll(9)

        # then
        self.assertEqual(['X','','X','','X','','X','','X','','X','','X','','X','','X','','X','X',9], self.b.getSymbols())
        self.assertEqual([30,60,90,120,150,180,210,240,270,299], self.b.getScores())        
    def testLastNoBonus(self):
        # when
        self._repeatRoll(9, 10)
        self.b.roll(9)
        self.b.roll(0)

        # then
        self.assertEqual(['X','','X','','X','','X','','X','','X','','X','','X','','X','',9,'-',''], self.b.getSymbols())
        self.assertEqual([30,60,90,120,150,180,210,239,258,267], self.b.getScores())        
    def testLastStrikeSpare(self):
        # when
        self._repeatRoll(10, 10)
        self.b.roll(5)
        self.b.roll(5)

        # then
        self.assertEqual(['X','','X','','X','','X','','X','','X','','X','','X','','X','','X',5,'/'], self.b.getSymbols())
        self.assertEqual([30,60,90,120,150,180,210,240,265,285], self.b.getScores())        
    def testLastSpareStrike(self):
        # when
        self._repeatRoll(9, 10)
        self.b.roll(5)
        self.b.roll(5)
        self.b.roll(10)

        # then
        self.assertEqual(['X','','X','','X','','X','','X','','X','','X','','X','','X','',5,'/','X'], self.b.getSymbols())
        self.assertEqual([30,60,90,120,150,180,210,235,255,275], self.b.getScores())
    def testNineSpareTenStrikes(self):
        # when
        self._repeatRoll(8, 10)
        self.b.roll(5)
        self.b.roll(5)
        self._repeatRoll(9, 10) # 3번만 해도 되는데 게임 끝났는지 로직이 잘되나 확인.
        # then
        self.assertEqual(['X','','X','','X','','X','','X','','X','','X','','X','',5,'/','X','X','X'], self.b.getSymbols())
        self.assertEqual([30,60,90,120,150,180,205,225,245,275], self.b.getScores())

    # 잘못된 수를 넣었을 때 Exception이 발생하는 지 여부.
    # 참조 : http://stackoverflow.com/questions/156503/how-do-you-assert-that-a-certain-exception-is-thrown-in-junit-4-tests
    # 질문 부분만 소스에서 참조함.
    def testValueError(self):
        thrown = False
        try:
            self.b.roll(-1)
            self.b.roll(11)
        except Exception:
            thrown = True
        self.assertTrue(thrown)
    def testValueError2(self):
        thrown = False
        try:
            self.b.roll('G')
        except Exception:
            thrown = True
        self.assertTrue(thrown)
    def testSpareError(self):
        thrown = False
        try:
            self.b.roll(5)
            self.b.roll(6)
        except Exception:
            thrown = True
        self.assertTrue(thrown)
    def testLastSpareError(self):
        thrown = False
        self._repeatRoll(10, 10)
        try:
            self.b.roll(5)
            self.b.roll(6)
        except Exception:
            thrown = True
        self.assertTrue(thrown)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()

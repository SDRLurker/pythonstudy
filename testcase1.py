#-*- coding: utf-8 -*-
'''
Created on 2016. 1. 20.

@author: donglyeolsin
'''
import unittest

class SubDate:
    @staticmethod
    # year(해당년도)가 윤년이면 True, 아니면 False
    def isLeapYear(year):
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        if year % 4 == 0:
            return True
        return False
    
    @staticmethod
    # 1년 1월 1일부터 year년 1월 1일까지 날짜수를 계산
    def getYearDay(year):
        result = 0
        for i in range(1,year):
            if SubDate.isLeapYear(i):  result += 366
            else:   result += 365
        return result
    
    @staticmethod
    # 1월 1일부터 month월 1일까지 날짜수를 계산.
    # 윤년이면 month가 3월 이상일 때 1 증가함.
    def getMonthDay(month, isLeap):
        monthDays = (31,28,31,30,31,30,31,31,30,31,30,31)
        result = 0
        for i in range(1,month):
            result = result + monthDays[i-1]
        if month > 2 and isLeap == True:
            result = result + 1
        return result
        
    @staticmethod
    # 1년 1월 1일부터 date 날짜까지 전체 날짜 수를 계산.
    def getTotalDay(date):
        year=int(date[:4])
        month=int(date[4:6])
        day=int(date[6:8])
        return SubDate.getYearDay(year) + SubDate.getMonthDay(month, SubDate.isLeapYear(year)) + day

    @staticmethod
    # a 날짜에서 b 날짜의 차이를 계산.
    def sub(a,b):
        return abs(SubDate.getTotalDay(a)-SubDate.getTotalDay(b))

class Test(unittest.TestCase):
    def testGetYearDay(self):
        self.assertEqual(0, SubDate.getYearDay(1))
        self.assertEqual(365, SubDate.getYearDay(2))
        self.assertEqual(365+365+365+366, SubDate.getYearDay(5))
    def testLeapYear(self):
        self.assertTrue(SubDate.isLeapYear(0))
        self.assertFalse(SubDate.isLeapYear(1))
        self.assertTrue(SubDate.isLeapYear(4))
        self.assertTrue(SubDate.isLeapYear(1200))
        self.assertFalse(SubDate.isLeapYear(700))
    def testGetMonthDay(self):
        self.assertEqual(0, SubDate.getMonthDay(1, True))
        self.assertEqual(31, SubDate.getMonthDay(2, False))
    def testGetTotalDay(self):
        self.assertEqual(1, SubDate.getTotalDay("00010101"))
        self.assertEqual(366, SubDate.getTotalDay("00020101"))
    def testSubDate(self):
        self.assertEqual(1, SubDate.sub("20061231", "20070101"))
        self.assertEqual(31+28+30+31+14, SubDate.sub("20070101", "20070515"))
        self.assertEqual(31+29+30+31+14, SubDate.sub("20080101", "20080515"))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
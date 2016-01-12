#-*- coding: utf-8 -*-
'''
Created on 2016. 1. 9.
@author: donglyeolsin
'''

from datetime import date
from calendar import monthrange

# get : start~end 구간에 대한 cterm 당기 구간에 속하는 manmonth를 구한다.
# start : 투입시작일. 튜플(yyyy,mm,dd)
# end : 투입종료일. 튜플(yyyy,mm,dd)
# cterm : 당기 구간, 날짜 타입에서 년도만 추출하여 당기 구간으로 사용한다.
# 리턴 : 당기 구간에 속하는 manmonth 리스트를 얻는다.
def get(start, end, cterm=date.today()):
    manmonth = [0 for x in range(12)]

    # start 투입시작일 값이 투입종료일보다 작아지도록 무조건 세팅한다. 반대 조건이면 swap한다.
    if start > end:
        start, end = end, start

    sterm = (cterm.year, 1, 1)
    eterm = (cterm.year, 12, 31)

    # 입력한 투입시작일/투입종료일을 date 타입의 sdate, edate 객체를 생성한다.
    sdate = date(start[0],start[1],start[2])
    edate = date(end[0],end[1],end[2])
    print start, end, sterm, eterm
    
    # 투입시작일~투입종료일이 당기 구간에 속하지 않으면 pass
    if end < sterm or start > eterm:
        pass
    # 투입 중간부터 투입종료일만 당기 구간에 속할경우 
    elif start < sterm and end <= eterm:
        for i in range(edate.month):
            if i+1 == edate.month:
                manmonth[i] = edate.day / float(monthrange(edate.year, edate.month)[1]) 
                break
            else:
                manmonth[i] = 1
    # 투입시작일~투입종료일이 당기 구간에 포함될 경우
    elif start >= sterm and end <= eterm:
        for i in range(edate.month):
            if i+1 == sdate.month:
                manmonth[i] = 1 - (sdate.day / float(monthrange(sdate.year, sdate.month)[1]))
            elif i+1 == edate.month:
                manmonth[i] = edate.day / float(monthrange(edate.year, edate.month)[1])
                break
            elif i+1 > sdate.month and i+1 < edate.month:
                manmonth[i] = 1
    # 투입시작일부터 투입 중간까지 당기 구간에 속할 경우
    elif start >= sterm and end > eterm:
        for i in range(sdate.month-1,12):
            if i+1 == sdate.month:
                manmonth[i] = 1 - (sdate.day / float(monthrange(sdate.year, sdate.month)[1]))
            else:
                manmonth[i] = 1
                
    return manmonth
    
if __name__ == '__main__':
    s=(2016,2,14)
    e=(2016,12,10)
    manmonth = get(s,e)
    print manmonth
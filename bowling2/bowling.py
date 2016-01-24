﻿# -*- coding: utf-8 -*-
class Bowling:
    def __init__(self):
        self.turn = 0
        self.turns = [0 for x in range(21)]
        
        self.currentFrame = 1   # 칠 차례 기준
        self.turnInFrame = 1    # 현재 프레임 내 몇 번째 인지
        self.rolls = ['' for x in range(21)]
        self.scores = ['' for x in range(10)]
        
    def _isStrikeTil9(self, pins):  # 9프레임 까지 스트라이크
        return self.currentFrame <= 9 and self.turnInFrame == 1 and pins == 10
    def _isStrikeAt10(self, pins):
        return self.currentFrame == 10 and pins == 10
    
    def roll(self, pins):
        self.turns[self.turn] = pins
        self.turn += 1
        
        if self._isStrikeTil9(pins):
            self.rolls[(self.currentFrame-1)*2] = 'X'
            self.currentFrame += 1
        elif self._isStrikeAt10(pins):
            self.rolls[(self.currentFrame-1)*2+(self.turnInFrame-1)] = 'X'
            self.turnInFrame += 1
        else:
            self.rolls[(self.currentFrame-1)*2+(self.turnInFrame-1)] = pins
            if self.turnInFrame == 1:   
                self.currentFrame += 1
                self.turnInFrame += 1
            else:
                self.turnInFrame = 1
        
    def getRolls(self):
        return self.rolls
    
    def getScores(self):
        return self.scores
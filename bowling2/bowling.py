# -*- coding: utf-8 -*-
class Bowling:
    def __init__(self):
        self.turn = 0
        self.turns = [0 for x in range(21)]

        self.currentFrame = 1   # 칠 차례 기준
        self.turnInFrame = 1    # 현재 프레임 내 몇 번째 인지
        self.symbols = ['' for x in range(21)]
        self.scores = ['' for x in range(10)]

    def _isStrikeTil9(self, pins):  # 9프레임 까지 스트라이크
        return self.currentFrame <= 9 and self.turnInFrame == 1 and pins == 10
    def _isStrikeAt10(self, pins):
        return self.currentFrame == 10 and pins == 10
    def _isSpare(self):
        return self.turnInFrame >= 2 and sum(self.turns[self.turn-1:self.turn+1]) == 10
        
    def _getSymbolIndex(self):
        return (self.currentFrame-1)*2+(self.turnInFrame-1)
    def _isStrikeAtTurn_2(self):    # 2번째 이전 투구가 스트라이크일 때
        return self.turn >= 2 and self._isStrikeTil9(self.turns[self.turn-2])
    

    def roll(self, pins):
        self.turns[self.turn] = pins

        if self._isStrikeTil9(pins):
            self.symbols[self._getSymbolIndex()] = 'X'
            self.currentFrame += 1
        elif self._isStrikeAt10(pins):
            self.symbols[self._getSymbolIndex()] = 'X'
            self.turnInFrame += 1
        else:
            if self._isSpare():
                self.symbols[self._getSymbolIndex()] = '/'
            else:
                self.symbols[self._getSymbolIndex()] = pins
            
            if self.turnInFrame == 1:   
                self.turnInFrame += 1
                # 바로 이전 투구가 스페어일 때
                sym_idx = self._getSymbolIndex() 
                # 스페어 점수 계산
                print self.currentFrame, sym_idx, self.symbols[sym_idx-1]
                if sym_idx > 1 and self.symbols[sym_idx-1] == '/':
                    self.scores[self.currentFrame-1] = self.scores[self.currentFrame-2] + sum(self.turns[self.turn-1:self.turn+1])           
            # 10프레임 조건 추가 필요. 
            
            else:
                # 스트라이크 점수 계산
                self.turnInFrame = 1
                if self._isStrikeAtTurn_2():    
                    self.scores[self.currentFrame-2] = sum(self.turns[self.turn-2:self.turn+1])
                # 스페어가 아닐 경우에만 현재프레임 점수 계산
                if sum(self.turns[self.turn-1:self.turn+1]) < 10:   
                    self.scores[self.currentFrame-1] = self.scores[self.currentFrame-2] + sum(self.turns[self.turn-1:self.turn+1])

                self.currentFrame += 1

        self.turn += 1

    def getSymbols(self):
        return self.symbols

    def getScores(self):
        return self.scores

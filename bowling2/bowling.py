# -*- coding: utf-8 -*-
class Bowling:
    def __init__(self):
        self.turn = 0
        self.turns = [0 for x in range(21)]

        self.currentFrame = 1   # 칠 차례 기준
        self.turnInFrame = 1    # 현재 프레임 내 몇 번째 인지
        self.symbols = ['' for x in range(21)]
        self.scores = ['' for x in range(10)]
        
        self.turnStrike = -1
        self.turnSpare = -1
        self.scoreIdx = 0

    def _isStrikeTil9(self, pins):  # 9프레임 까지 스트라이크
        return self.currentFrame <= 9 and self.turnInFrame == 1 and pins == 10
    def _isStrikeAt10(self, pins):
        return self.currentFrame == 10 and pins == 10
    def _isSpareTil9(self):
        return self.turnInFrame == 2 and sum(self.turns[self.turn-1:self.turn+1]) == 10
    def _isSpareAt10(self):
        if self.turnInFrame == 2:
            return self.turns[self.turn-1] < 10 and sum(self.turns[self.turn-1:self.turn+1]) == 10
        elif self.turnInFrame == 3:
            return sum(self.turns[self.turn-2:self.turn])!= 10 and sum(self.turns[self.turn-1:self.turn+1]) == 10
        else:
            return False
        
    def _getSymbolIndex(self):
        return (self.currentFrame-1)*2+(self.turnInFrame-1)
    
    def _getLastScore(self):
        lastScore = 0
        if self.scoreIdx > 0:
             lastScore = self.scores[self.scoreIdx-1] 
        return lastScore;

    def roll(self, pins):
        if pins == 'F':
            self.turns[self.turn] = 0
        else:
            self.turns[self.turn] = pins

        if self.currentFrame <= 9:
            # 전처리            
            if self._isStrikeTil9(pins):
                # 심볼로직
                self.symbols[self._getSymbolIndex()] = 'X'
                # 스트라이크인 turn 위치를 기억해 놓음.
                if self.turnStrike == -1:
                    self.turnStrike = self.turn
            else:
                # 심볼로직   
                if pins == 0:
                    self.symbols[self._getSymbolIndex()] = '-'
                elif self._isSpareTil9():
                    self.symbols[self._getSymbolIndex()] = '/'
                else:
                    self.symbols[self._getSymbolIndex()] = pins                
                
            # 스트라이크 과거 점수처리    
            if self.turnStrike >=0 and self.turn == self.turnStrike + 2:
                lastScore = self._getLastScore()
                self.scores[self.scoreIdx] = lastScore + sum(self.turns[self.turnStrike:self.turn+1])
                self.scoreIdx += 1
                # 콤보 이상이면 strikeIdx 유지. 그렇지 않으면 초기화.
                if self.turns[self.turnStrike+1] == 10:
                    self.turnStrike += 1
                else:
                    self.turnStrike = -1
            # 스페어  과거 점수처리
            
            # 일반점수처리
            if self.turnInFrame == 2 and not self._isSpareTil9() and not self._isSpareTil9():
                lastScore = self._getLastScore()
                self.scores[self.scoreIdx] = lastScore + sum(self.turns[self.turn-1:self.turn+1])
                self.scoreIdx += 1
                
            # 후처리 : 다음처리를 계산
            if self._isStrikeTil9(pins):
                self.currentFrame += 1
            else:
                self.turnInFrame += 1
                if self.turnInFrame > 2:
                    self.turnInFrame = 1
                    self.currentFrame += 1
            
        elif self.currentFrame == 10:
            # 심볼로직
            if self._isSpareAt10(): # 스페어처리가 스트라이크 처리 계산보다 우선순위 높음.
                self.symbols[self._getSymbolIndex()] = '/'
            elif self._isStrikeAt10(pins):
                self.symbols[self._getSymbolIndex()] = 'X'
            else:
                self.symbols[self._getSymbolIndex()] = pins
            
            self.turnInFrame += 1
            
            # 게임 끝났는지 조건 확인 필요.
            # 점수계산로직
            
        self.turn += 1

    def getSymbols(self):
        return self.symbols

    def getScores(self):
        return self.scores

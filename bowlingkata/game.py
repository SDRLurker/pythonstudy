class Game:
    def __init__(self):
        self.rolls = [0 for k in range(21)]
        self.currentRoll = 0
    def roll(self, pins):
        self.rolls[self.currentRoll] = pins
        self.currentRoll += 1

    def _isStrike(self, frameIndex):
        return self.rolls[frameIndex] == 10
    def _strikeBonus(self, frameIndex):
        return self.rolls[frameIndex+1] + self.rolls[frameIndex+2]
    def _isSpare(self, frameIndex):
        return self.rolls[frameIndex] + self.rolls[frameIndex+1] == 10
    def _spareBonus(self, frameIndex):
        return self.rolls[frameIndex+2]
    def _sumOfBallsInFrame(self, frameIndex):
        return self.rolls[frameIndex] + self.rolls[frameIndex+1]
    
    def score(self):
        s = 0
        frameIndex = 0
        for frame in range(10):
            if self._isStrike(frameIndex):    # strike
                s += (10 + self._strikeBonus(frameIndex))
                frameIndex += 1
            elif self._isSpare(frameIndex):
                s += (10 + self._spareBonus(frameIndex))
                frameIndex += 2
            else:
                s += self._sumOfBallsInFrame(frameIndex)
                frameIndex += 2
        return s
class Game:

    def __init__(self):
        self.__currentRoll = 0
        self.__rolls = [0 for i in range(21)]

    def roll(self, pins):

        self.__rolls[self.__currentRoll] = pins
        self.__currentRoll += 1

    def score(self):

        self.score = 0
        self.frameIndex = 0

        for frame in range(10):
            if self.__isStrike(self.frameIndex):
                self.score += 10 + \
                              self.__rolls[self.frameIndex + 1] + \
                              self.__rolls[self.frameIndex + 2]

                self.frameIndex += 1


            elif self.__isSpare(self.frameIndex):
                self.score += 10 + self.__rolls[self.frameIndex + 2]
                self.frameIndex += 2
            else:
                self.score += self.__rolls[self.frameIndex] + self.__rolls[self.frameIndex + 1]
                self.frameIndex += 2

        return self.score

    def __isStrike(self, frameIndex):
        return self.__rolls[frameIndex] == 10

    def __isSpare(self, frameIndex):
        return self.__rolls[frameIndex] + self.__rolls[frameIndex + 1] == 10

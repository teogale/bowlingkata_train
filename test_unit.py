import unittest
from bowling_game import Game



class BowlingGameTest(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def __RollMany(self,n,pins):
        for i in range(n):
            self.game.roll(pins)

    def test_GutterGame(self):
        self.__RollMany(20,0)
        self.assertEquals(0, self.game.score())

    def test_AllOnes(self):
        self.__RollMany(20, 1)
        self.assertEquals(20, self.game.score())

    def test_OneSpare(self):
        self.__RollSpare()
        self.game.roll(3)
        self.__RollMany(17, 0)
        self.assertEquals(16, self.game.score())

    def test_PerfectionGame(self):

        self.__RollMany(12,10)
        self.assertEquals(300, self.game.score())

    def test_OneStrike(self):

        self.__RollStrike()
        self.game.roll(3)
        self.game.roll(4)
        self.__RollMany(16,0)
        self.assertEquals(24, self.game.score())

    def __RollStrike(self):
        self.game.roll(10)

    def __RollSpare(self):
        self.game.roll(5)
        self.game.roll(5)


if __name__ == '__main__':
    unittest.main()







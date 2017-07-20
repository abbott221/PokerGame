import unittest
import Game

class GameTester(unittest.TestCase):
    def testGameExists(self):
        game = Game.Game()
        self.assertTrue(game is not None)


    def testGameHasPlayers(self):
        game = Game.Game()
        self.assertTrue(game.players is not None)

if __name__ == '__main__':
    unittest.main()
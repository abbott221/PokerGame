import unittest
import Player


# Example class for setting up unit testing in python
class PlayerTester(unittest.TestCase):

    def testHand(self):
        player = Player.Player();
        assertIsNotNone(player.hand);

    def testBalance(self):
        player = Player.Player();
        self.assertIsNotNone(player.balance);

if __name__ == '__main__':
    unittest.main()
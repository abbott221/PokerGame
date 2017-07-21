import unittest
import CLIPrompter
from Card import Rank, Suit, Card
from Hand import Hand

class CLIPrompterTester(unittest.TestCase):
    def setUp(self):
        # self.game = Game()
        self.cliPrompt = CLIPrompter.CLIPrompter()
        self.cards = [Card(Rank.TWO, Suit.HEARTS), Card(Rank.SEVEN, Suit.CLUBS), 
        Card(Rank.KING, Suit.CLUBS), Card(Rank.FIVE, Suit.DIAMONDS), 
        Card(Rank.JACK, Suit.SPADES)]
        self.hand = Hand(self.cards)

    def test_printHand_PrintHandContent(self):
        self.assertEqual(self.cliPrompt.printHand(self.hand.cards), '2-H, 7-C, K-C, 5-D, J-S') 

    def test_promptNumUsers_Return2(self):
        print('return 2 test')
        self.assertEqual(self.cliPrompt.promptNumberPlayers(), 2)

    def test_promptNumUsers_ReturnNeg1(self):
        print('return -1 test')
        self.assertEqual(self.cliPrompt.promptNumberPlayers(), -1)


if __name__ == '__main__':
    unittest.main()
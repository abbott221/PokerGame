import unittest
import Card

#testing push
# Example class for setting up unit testing in python
class CardTester(unittest.TestCase):

    def testAceLessThanKing(self):
        card1 = Card.Card(Card.Rank.ACE, Card.Suit.SPADES)
        card2 = Card.Card(Card.Rank.KING, Card.Suit.DIAMONDS)
        self.assertTrue(card1.rank > card2.rank)

if __name__ == '__main__':
    unittest.main()
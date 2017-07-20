import unittest
import Card
import Hand

#testing push
# Example class for setting up unit testing in python
class HandTester(unittest.TestCase):

    def testHandSorted(self):
        hand = Hand.Hand([Card.Card(Card.Rank.JACK, Card.Suit.SPADES), \
            Card.Card(Card.Rank.ACE, Card.Suit.SPADES), \
            Card.Card(Card.Rank.FIVE, Card.Suit.SPADES), \
            Card.Card(Card.Rank.ACE, Card.Suit.SPADES), \
            Card.Card(Card.Rank.FOUR, Card.Suit.SPADES)])
        self.assertTrue(hand.cards[0].rank >= hand.cards[1].rank >=	hand.cards[2].rank >= hand.cards[3].rank >= hand.cards[4].rank)

if __name__ == '__main__':
    unittest.main()
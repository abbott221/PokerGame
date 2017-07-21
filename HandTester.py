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
            Card.Card(Card.Rank.QUEEN, Card.Suit.SPADES), \
            Card.Card(Card.Rank.FOUR, Card.Suit.SPADES)])
        self.assertTrue(hand.cards[0].rank >= hand.cards[1].rank >=	\
        	hand.cards[2].rank >= hand.cards[3].rank >= hand.cards[4].rank)

    def testHighCard(self):
    	hand1 = Hand.Hand([Card.Card(Card.Rank.JACK, Card.Suit.SPADES), \
            Card.Card(Card.Rank.KING, Card.Suit.SPADES), \
            Card.Card(Card.Rank.FIVE, Card.Suit.SPADES), \
            Card.Card(Card.Rank.QUEEN, Card.Suit.HEARTS), \
            Card.Card(Card.Rank.FOUR, Card.Suit.SPADES)])
    	hand2 = Hand.Hand([Card.Card(Card.Rank.JACK, Card.Suit.SPADES), \
            Card.Card(Card.Rank.ACE, Card.Suit.SPADES), \
            Card.Card(Card.Rank.FIVE, Card.Suit.SPADES), \
            Card.Card(Card.Rank.QUEEN, Card.Suit.SPADES), \
            Card.Card(Card.Rank.FOUR, Card.Suit.DIAMONDS)])
    	self.assertTrue(hand1.value == Hand.Value.HIGH_CARD)
    	self.assertTrue(hand1.compareTo(hand2) < 0)
if __name__ == '__main__':
    unittest.main()
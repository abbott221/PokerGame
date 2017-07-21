import unittest
import Deck


# Example class for setting up unit testing in python
class DeckTester(unittest.TestCase):

    def testDeckExists(self):
        deck = Deck.Deck()
        self.assertIsNotNone(deck)
        self.assertEqual(deck.deckLength(), 0)

    def testPopulateDeck(self):
        deck = Deck.Deck()
        deck.populateDeck()
        self.assertEqual(deck.deckLength(), 52)

    def testDealCard(self):
        deck = Deck.Deck()
        deck.populateDeck()
        card = deck.dealCard()
        self.assertIsNotNone(card)

    def testDealCardMoreThan52(self):
        deck = Deck.Deck()
        deck.populateDeck()
        for _ in range(52):
            card = deck.dealCard()
        self.assertEqual(deck.dealCard(), 'All cards have been dealt')

    def testDeckIsShuffled(self):
        deck = Deck.Deck()
        deck.populateDeck(2, 14, 1, 1)
        shuffled = False
        
        currentCard = deck.dealCard()
        for _ in range(2, 14):
            nextCard = deck.dealCard()
            if currentCard.rank + 1 != nextCard.rank:
                shuffled = True
                break
        self.assertTrue(shuffled)
        





if __name__ == '__main__':
    unittest.main()
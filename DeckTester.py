import unittest
import Deck


# Example class for setting up unit testing in python
class DeckTester(unittest.TestCase):

    def testDeckExists(self):
        deck = Deck.Deck()
        self.assertIsNotNone(deck)
        self.assertEquals(deck.deckLength(), 0)

    def testPopulateDeck(self):
        deck = Deck.Deck()
        deck.populateDeck()
        self.assertEqual(deck.deckLength(), 52)

    def testDealCard(self):
        deck = Deck.Deck()
        deck.populateDeck()
        card = deck.dealCard()
        self.assertIsNotNone(card)

    # def testDeckIsShuffled():
    #     deck = Deck.Deck()
    #     deck.populateDeck(2, 14, 1, 1)
    #     currentCard = deck.dealCard()
        





if __name__ == '__main__':
    unittest.main()
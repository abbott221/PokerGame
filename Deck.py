import Card
import random

class Deck:

	def __init__(self):
		self.cards = []

	def populateDeck(self, lowestRank = 2, highestRank = 14, lowestSuit = 1, highestSuit = 4):
		for rank in range(lowestRank, highestRank + 1):
			for suit in range(lowestSuit, highestSuit + 1):
				card = Card.Card(rank, suit)
				self.cards.append(card)

		random.shuffle(self.cards)		

	def dealCard(self):
		try:
			topCard = self.cards.pop()
			return topCard
		except IndexError:
			print('All cards have been dealt')

	def deckLength(self):
		return len(self.cards)


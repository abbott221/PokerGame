import Card
from enum import IntEnum

class Value(IntEnum):
	HIGH_CARD = 1
	PAIR = 2
	TWO_PAIR = 3
	THREE_OF_A_KIND = 4
	FULL_HOUSE = 5
	STRAIGHT = 6
	FLUSH = 7
	FOUR_OF_A_KIND = 8
	STRAIGHT_FLUSH = 9

class Hand:
	def __init__(self, cards):
		self.cards = sorted(cards, key=lambda x: x.rank, reverse=True)
		self.value = 0;
		self.tiebreaker = [0] * 5
		if self.isStraightFlush():
			self.labelStraightFlush()
		elif self.isFourOfAKind():
			self.labelFourOfAKind()
		elif self.isFlush():
			self.labelFlush()
		elif self.isStraight():
			self.labelStraight()
		elif self.isFullHouse():
			self.labelFullHouse()
		elif self.isThreeOfAKind():
			self.labelThreeOfAKind() 
		elif self.isTwoPair():
			self.labelTwoPair() 
		elif self.isPair():
			self.labelPair() 
		else:
			self.labelHighCard()

	def compareTo(self, hand2):
		if self.value > hand2.value:
			return 1
		elif self.value < hand2.value:
			return -1
		else:
			for i in range(0, 4):
				if self.tiebreaker[i] > hand2.tiebreaker[i]:
					return 1
				elif self.tiebreaker[i] < hand2.tiebreaker[i]:
					return -1
			return 0


	def isStraightFlush(self):
		return
	def labelStraightFlush(self):
		return
	def isFourOfAKind(self):
		return
	def labelFourOfAKind(self):
		return
	def isFlush(self):
		return
	def labelFlush(self):
		return
	def isStraight(self):
		return
	def labelStraight(self):
		return
	def isFullHouse(self):
		return
	def labelFullHouse(self):
		return
	def isThreeOfAKind(self):
		return
	def labelThreeOfAKind(self):
		return 
	def isTwoPair(self):
		return
	def labelTwoPair(self):
		return 
	def isPair(self):
		return
	def labelPair(self):
		return 
	def labelHighCard(self):
		self.value = Value.HIGH_CARD
		for i in range(0, 4):
			self.tiebreaker[i] = self.cards[i].rank

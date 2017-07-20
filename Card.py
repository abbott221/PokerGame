from enum import IntEnum
class Rank(IntEnum):
	ACE = 14
	KING = 13
	QUEEN = 12
	JACK = 11
	TEN = 10
	NINE = 9
	EIGHT = 8
	SEVEN = 7
	SIX = 6
	FIVE = 5
	FOUR = 4
	THREE = 3
	TWO = 2

class Suit(IntEnum):
	DIAMONDS = 1
	CLUBS = 2
	HEARTS = 3
	SPADES = 4

class Card:
	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit
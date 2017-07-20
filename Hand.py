import Card
class Hand:
	def __init__(self, cards):
		self.cards = sorted(cards, key=lambda x: x.rank, reverse=True)
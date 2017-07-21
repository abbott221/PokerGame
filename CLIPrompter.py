from Card import Rank, Suit
from Hand import Hand
from Game import Game
from Player import Player

class CLIPrompter():

	def promptNumberPlayers(self):
		print('Hello. Would you like to play some poker?')
		num = int(input('How many humans are playing today? \nValid values are 2, 3, or 4.\n'))
		return num if ( 1 < num < 5) else -1

	def printHand(self, cards):
		msg = ''
		for card in cards[:-1]:
			msg = msg + str(card.rank.name)+'-'+str(card.suit.name)+', '
		msg = msg + str(cards[-1].rank.name)+'-'+str(cards[-1].suit.name)
		return msg

	def printWinnerAndBalanceInfo(self, winnerId, game):
		print('Player '+str(winnerId)+' wins this round!')
		for i, player in eumerate(game.players):
			print('Player '+str(i)+' balance: '+player.balance)


if __name__ == '__main__':
	prompter = CLIPrompter()
	prompter.printWinnerAndPotInfo(1)
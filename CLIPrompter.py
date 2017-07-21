

class CLIPrompter():

	def promptNumberPlayers(self):
		print('Hello. Would you like to play some poker?')
		num = int(input('How many humans are playing today? \nValid values are 2, 3, or 4.\n'))
		return num if ( 1 < num < 5) else -1

if __name__ == '__main__':
	prompter = CLIPrompter()
	prompter.promptNumberPlayers()
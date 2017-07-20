import unittest
import CLIPrompter
# import Game

class CLIPrompterTester(unittest.TestCase):
    def setUp(self):
        # self.game = Game()
        self.cliPrompt = CLIPrompter.CLIPrompter()

    def test_greet_ReturnHelloMsg(self):
        self.assertEqual(self.cliPrompt.greet(), 'Hello. Would you like to play some poker?')

    def test_printHand_PrintHandContent(self):
        self.assertEqual(self.cliPrompt.printHand(1), '2-H, 7-C, K-C, 5-D, J-S') 

    def test_promptNumUsers_Return5(self):
        self.assertEqual(self.cliPrompt.promptNumberPlayers(), 2)

if __name__ == '__main__':
    unittest.main()
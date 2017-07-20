import unittest
import CLIPrompter
# import Game

class CLIPrompterTester(unittest.TestCase):
    def setUp(self):
        # self.game = Game()
        self.cliPrompt = CLIPrompter()

    def tearDown(self):
        self.cliPrompt.dispose()

    def test_greet_ReturnHelloMsg(self):
        self.assertEqual(self.cliPrompt.greet(), 'Hello. Would you like to play some poker?')

    def test_printHand_PrintHandContent(self):
        self.assertEqual(self.cliPrompt.printHand(1), '2-H, 7-C, K-C, 5-D, J-S')

    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()
import unittest


# Example class for setting up unit testing in python
class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')

    def tearDown(self):
        self.widget.dispose()

if __name__ == '__main__':
    unittest.main()
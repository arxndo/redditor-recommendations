from NeoReddit import NeoReddit
from Configuration import Configuration
import unittest

class NeoReddit_test(unittest.TestCase):

    def setUp(self):
        cfg = Configuration.configuration('config.yml')
        self.nr = NeoReddit(cfg)

    def test_authorToSubs(self):
        authorName = 'kn0thing'
        expectedList = [('blog', 21106), \
                        ('reddit.com', 11026), \
                        ('photoshopbattles', 7950)]

        for result, expected in zip(self.nr.authorToSubs(authorName, 3), expectedList):
            self.assertEqual(result[0], expected[0])
            self.assertEqual(result[1], expected[1])


if __name__ == '__main__':
    unittest.main()

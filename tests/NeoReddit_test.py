from NeoReddit import NeoReddit
from utils.classes.Configuration import Configuration
import unittest

class NeoReddit_test(unittest.TestCase):

    def setUp(self):
        cfg = Configuration.configuration('/home/ubuntu/redditor-recommendations/config.yml')
        self.nr = NeoReddit(cfg)


    def compareLists(self, expectedList, actualList):
        for actual, expected in zip(actualList, expectedList):
            self.assertEqual(actual[0], expected[0])
            self.assertEqual(actual[1], expected[1])


    def test_authorToSubs(self):
        authorName = 'kn0thing'
        expectedList = [('blog', 21106), \
                        ('reddit.com', 11026), \
                        ('photoshopbattles', 7950)]

        actualList = self.nr.authorToSubs(authorName, 3)

        self.compareLists(expectedList, actualList)


    def test_subToAuthors(self):
        subName = 'Patriots'
        expectedList = [('swantonsoup', 36244), \
                        ('lordmadone', 31297), \
                        ('douglasmacarthur', 27439)]

        actualList = self.nr.subToAuthors(subName, 3)
        self.compareLists(expectedList, actualList)

    def test_authorToAuthors(self):
        authorName = 'williamshatner'
        expectedList = [('PeterMayhew', 47773), \
                        ('williamshatner', 6852), \
                        ('redtaboo', 8826), \
                        ('united1020', 46618), \
                        ('wil', 31172)]

        actualList = self.nr.authorToAuthors(authorName, 5)
        self.compareLists(expectedList, actualList)


    def test_cosineSimilarity(self):
        author1 = 'kn0thing'
        author2 = 'GovSchwarzenegger'
        expected = 0.97
        actual = self.nr.cosineSimilarity(author1, author2)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()

from src.download.classes.RawComments import RawComments
from src.utils.Configuration import Configuration
import json
import os
import unittest

class RawComments_test(unittest.TestCase):

    def setUp(self):
        path = '/home/ubuntu/redditor-recommendations/tests'
        self.cfg = Configuration.configuration('%s/test_config.yml' % path)
        self.processor = RawComments(self.cfg)

    def test_process(self):
        self.processor.process(self.cfg['dates']['startDate'], self.cfg['dates']['endDate'])
        os.system('aws s3 mv s3://romeostestbucket/RC_2005-12 . > /dev/null 2>&1')
        os.system('cat RC_2005-12 | head -1 >> test.json') 
        with open('test.json') as testJSON:
            data = json.load(testJSON)

        actual = data['body']
        expected = 'A look at Vietnam and Mexico exposes the myth of market liberalisation.'
        self.assertEqual(expected, actual)

    def tearDown(self):
        os.system('rm RC_2005-12')
        os.system('rm test.json')
        os.system('rm -rf files.pushshift.io')

if __name__ == '__main__':
    unittest.main()

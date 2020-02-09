import os
from Configuration import Configuration

class Importer:

    def __init__(self, cfg):
        self.bucket = cfg['s3']['merged'] 
        self.nodes1 = 'authors'
        self.nodes2 = 'subs'
        self.edges = 'author-sub'

    def process(self, startDate, endDate):
        self.startDate = startDate
        self.endDate = endDate
        if not os.path.isfile('tmp'):
            os.system('mkdir tmp')
        for name in [self.nodes1, self.nodes2]:
            self.download(name)

    def download(self, name):
        dirName = '%s_%s_%s' % (name, self.startDate, self.endDate)
        options = '--recursive --exclude "*" --include "*.csv"'
        os.system('aws s3 cp s3://%s/%s/ tmp %s' \
                % (self.bucket, dirName, options)) 
        os.system('mv ~/redditor-recommendations/tmp/part* tmp/%s.csv' % name)
        #os.system('rm -rf tmp')

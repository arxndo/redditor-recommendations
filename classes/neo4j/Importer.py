import os
from Configuration import Configuration

class Importer:

    def __init__(self, cfg):
        self.bucket = cfg['s3']['merged'] 
        self.nodes1 = 'authors'
        self.nodes2 = 'subs'
        self.edges = 'author-sub'
        self.path = '~/redditor-recommendations'

    def process(self, startDate, endDate):
        self.startDate = startDate
        self.endDate = endDate
        self.downloadAll() \
            .toDatabase()
        #self.cleanUp()

    def downloadAll(self):
        if not os.path.isdir('%s/tmp' % self.path):
            for name in [self.nodes1, self.nodes2, self.edges]:
                self.download(name)
        return self

    def download(self, name):
        dirName = '%s_%s_%s' % (name, self.startDate, self.endDate)
        options = '--recursive --exclude "*" --include "*.csv"'
        os.system('aws s3 cp s3://%s/%s/ tmp %s' \
                % (self.bucket, dirName, options)) 
        os.system('mv tmp/part*.csv tmp/%s.csv' %  name)
        #os.system('rm -rf tmp')

    def cleanUp(self):
        pass

    def toDatabase(self):
        os.system('sudo /usr/bin/neo4j stop')
        os.system('sudo /usr/bin/neo4j-admin import --nodes:author="headers/authors_header.csv,tmp/authors.csv" --nodes:subreddit="headers/subs_header.csv,tmp/subs.csv" --relationships:post_to="headers/author-sub_header.csv,tmp/author-sub.csv" --ignore-duplicate-nodes true --ignore-missing-nodes true')
        os.system('sudo /usr/bin/neo4j start')
        return self

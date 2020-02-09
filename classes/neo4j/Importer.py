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
        for name in [self.nodes1, self.nodes2, self.edges]:
            self.download(name)

    def download(name):
        dirName = '%s_%s_%s' % (name, self.startDate, self.endDate)
        os.system('mkdir tmp')
        os.system('aws s3 cp s3://%s/%s/*.csv tmp' dirName) 
        #os.system('rm -rf tmp')

if __name__ == '_main_':
        os.environ['PYSPARK_PYTHON'] = '/usr/bin/python3.5'
        os.environ["PYSPARKDRIVER_PYTHON"]= "/usr/bin/python3.5"]
        cfg = Configuration.configuration('config.yml')
        importer = Importer(cfg)
        importer.process(cfg['dates']['startDate'], cfg['dates']['endDate'])

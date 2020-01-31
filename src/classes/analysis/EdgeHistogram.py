from Calendar import Calendar
from pandas import pandas
from matplotlib import pyplot

class EdgeHistogram:
    """ Creates histogram of edge weights"""
 
    def __init__(self, cfg):
        self.inBucket = cfg['s3']['mergedEdgesBucket']
        self.outBucket = cfg['s3']['analysisBucket']


    def process(self, startDate, endDate):
        """ Histogram of edges from startDate to endDate"""
        self.ingest(startDate, endDate) \
            .transform() \
            .write(startDate, endDate)


    def ingest(self, startDate, endDate):
        """ Read merged edges """

        self.df = pandas \
                  .read_parquet('s3a://%s/%s_%s' 
                        % (self.inBucket, startDate, endDate))
        return self


    def transform(self):
        """ Create histogram """

        self.hist = self.df['weight'].hist()
        return self


    def write(self, startDate, endDate):
        """ Save plot to s3 """

        fig = self.hist.get_figure()
        fig.savefig('s3a://%s/%s_%s' \
                % (self.outBucket, startDate, endDate))


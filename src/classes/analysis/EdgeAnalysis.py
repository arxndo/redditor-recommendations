from pyspark.sql.functions import concat, col
from Sequentiable import Sequentiable

class EdgeAnalysis(Sequentiable):
    """ Analysis for pruning"""
 
    def __init__(self, context, cfg):
        self.context = context
        self.inBucket = cfg['s3']['edgesBucket']
        self.outBucket = cfg['s3']['analysisBucket']


    def ingest(self, date):
        """ Read edges """

        self.df = self.context.read.parquet('s3a://%s/%s' \
                % (self.inBucket, date))
        return self


    def transform(self, date):
        """ Sort """

        print('%s' % date)

        df = self.df.select('weight')
        print('%d, %d' % (0, df.count()))
        for i in range(1,10):
            df = df.where('weight > %d' % i)
            print('%d, %d' % (i, df.count()))
        return self


    def write(self, date):
        """ Do nothing """
        pass

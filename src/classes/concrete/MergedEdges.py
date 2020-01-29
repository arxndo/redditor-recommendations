from pyspark.sql import functions as F
from Sequentiable import Sequentiable

class MergedEdges(Sequentiable):
 
    def __init__(self, context, cfg):
        self.context = context
        self.inBucket = cfg['s3']['edgesBucket']
        self.outBucket = cfg['s3']['mergedEdgesBucket']


    def ingest(self, date)
        self.df = self.context \
                    .read \
                    .parquet \
                    .load('s3a://%s/%s', \
                        % (self.inBucket, date))

    def transform(self, date):
        pass

    def write(self, date):
        pass

    def merge(self):

        self.df \
        .groupBy('author_1', 'author_2') \
        .agg( {'weight' : 'sum'} ) \
        .withColumnRenamed('sum(weight)', 'weight') \
        .write \
        .parquet('s3a://%s/%s_%s' \
            % (self.outBucket, startDate, endDate))

        #.sort(F.desc('weight')) \

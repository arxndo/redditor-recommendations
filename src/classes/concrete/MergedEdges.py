from pyspark.sql import functions as F
from Sequentiable import Sequentiable

class MergedEdges:
""" Merge of edges across multiple months"""
 
    def __init__(self, context, cfg):
        self.context = context
        self.inBucket = cfg['s3']['edgesBucket']
        self.outBucket = cfg['s3']['mergedEdgesBucket']


    def ingest(self, startDate, endDate):
        """ Read parquet edge files """

        paths = Calendar.s3paths(self.inBucket, startDate, endDate)
        self.df = self.context.read.parquet(*paths)
        return self


    def transform(self):
        """ Merge by author pairs, add weights """

        self.df = self.df \
            .groupBy('author_1', 'author_2') \
            .agg( {'weight' : 'sum'} ) \
            .withColumnRenamed('sum(weight)', 'weight') 
        return self


    def write(self, startDate, endDate):
        """ Write to parquet s3 files """

        self.df \
        .write \
        .parquet('s3a://%s/%s_%s' \
            % (self.outBucket, startDate, endDate))
        return self


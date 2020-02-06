from pyspark.sql import functions as F
from Sequentiable import Sequentiable
from Calendar import Calendar

class MergedNodes:
    """ Merge of edges across multiple months"""
 
    def __init__(self, context, cfg):
        self.context = context
        self.inBucket = cfg['s3']['nodesBucket']
        self.outBucket = cfg['s3']['mergedNodesBucket']
        self.truncation = cfg['tuning']['truncation']

    def process(self, startDate, endDate):
        """ Merge from startDate to endDate"""
        self.ingest(startDate, endDate) \
            .transform() \
            .write(startDate, endDate)


    def ingest(self, startDate, endDate):
        """ Read parquet edge files """

        paths = Calendar.s3paths(self.inBucket, startDate, endDate)
        self.df = self.context.read.parquet(*paths)
        return self


    def transform(self):
        """ Merge by author, add weights """

        self.df = self.df \
            .groupBy('author') \
            .agg( F.sum('score').alias('score'))
        return self


    def write(self, startDate, endDate):
        """ Write to parquet s3 files """

        self.df \
        .repartition(1) \
        .write \
        .option('header', 'true') \
        .mode('overwrite') \
        .csv('s3a://%s/%s_%s' \
            % (self.outBucket, startDate, endDate))
        return self


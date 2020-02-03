from pyspark.sql import functions as F
from GraphObject import GraphObject

class Nodes(GraphObject):
 
    def __init__(self, cfg, context):
        super().__init__(context, \
                        cfg['s3']['cleanCommentsBucket'], \
                        cfg['s3']['nodesBucket'])
        self.partitions = cfg['tuning']['nodePartitions']

    def transform(self, date):
        self.df = self.df \
                .select('author', 'score') \
                .groupBy('author') \
                .agg(F.sum('score').alias('score'))
        return self

    def write(self, date):
        n = self.partitions
        self.df = self.df.repartition(n)
        self.df \
            .write \
            .parquet('s3a://%s/%s' \
                % (self.outBucket, date), mode='overwrite')

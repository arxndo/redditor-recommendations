from pyspark.sql import functions as F
from GraphObject import GraphObject
from MonthlyClock import MonthlyClock

class AuthorSubEdges(GraphObject):


    def __init__(self, cfg, context):
        self.context = context
        self.inBucket = cfg['s3']['cleanCommentsBucket']
        self.outBucket = cfg['s3']['relationshipsBucket']
        self.truncation = cfg['tuning']['truncation']
        self.partitions = cfg['tuning']['edgePartitions']
        self.clock = MonthlyClock()
 

    def transform(self, date):
        self.df = self.df \
                      .select('author', 'subreddit', 'score') \
                      .groupBy('author', 'subreddit') \
                      .agg(F.sum(F.col('score')).alias('score')) \
                      .where('score > %d' % self.truncation)
        return self

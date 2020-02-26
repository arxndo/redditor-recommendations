from pyspark.sql import functions as F
from GraphObject import GraphObject
from MonthlyClock import MonthlyClock

class AuthorSubEdges(GraphObject):
    """ Relationships between authors and subreddits.
    In particular, for any pair of author and subreddit,
    the cumulative score gained by that author from that
    subreddit is recorded (when the score is above the
    truncation level (set as a default to 1 in the standard
    configuration file."""

    def __init__(self, cfg, context):
        self.context = context
        self.inBucket = cfg['s3']['cleanComments']
        self.outBucket = cfg['s3']['relationships']
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

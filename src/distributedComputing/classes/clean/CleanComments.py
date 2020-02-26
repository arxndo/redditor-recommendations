from spark.classes.Batches import Batches
from utils.classes.MonthlyClock import MonthlyClock

class CleanComments(Batches):
    """ Comments removed of all information other than
    author, top level parent (ie link_id), score, 
    date of creation, subreddit, and upvotes """

    def __init__(self, cfg, context):
        self.context = context
        self.inBucket = cfg['s3']['rawComments']
        self.outBucket = cfg['s3']['cleanComments']
        self.clock = MonthlyClock()

    def ingest(self, date):
        self.df = self.context.read.json('s3a://%s/RC_%s' \
                % (self.inBucket, date))
        return self

    def transform(self, date):
        self.df = self.df \
                      .select('author', \
                              'link_id', \
                              'score', \
                              'created_utc', \
                              'subreddit', \
                              'ups') \
                      .where('author != "[deleted]"')
        return self

    def write(self, date):
        self.df \
            .write \
            .parquet('s3a://%s/%s' \
                % (self.outBucket, date), mode='overwrite')

from Batches import Batches
from MonthlyClock import MonthlyClock

class CleanComments(Batches):

    def __init__(self, cfg, context):
        super().__init__(MonthlyClock())
        self.context = context
        self.inBucket = cfg['s3']['rawCommentsBucket']
        self.outBucket = cfg['s3']['cleanCommentsBucket']

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

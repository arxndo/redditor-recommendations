from Sequentiable import Sequentiable

class CleanComments(Sequentiable):

    def __init__(self, cfg, context):

        self.context = context
        self.inBucket = cfg['s3']['rawCommentsBucket']
        self.outBucket = cfg['s3']['cleanCommentsBucket']

    def ingest(self, date):
        self.df = self.context.read.json('s3a://%s/RC_%s' \
                % (self.inBucket, date))
        return self

    def transform(self, date):
        self.df = self.df.select('author', 'link_id', 'score', 'subreddit')
        return self

    def write(self, date):
        self.df.show()
        self.df \
            .write \
            .parquet('s3a://%s/%s' \
                % (self.outBucket, date), mode='overwrite')

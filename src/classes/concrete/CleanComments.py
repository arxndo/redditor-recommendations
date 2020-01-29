from Sequentiable import Sequentiable

class CleanComments(Sequentiable):

    def __init__(self, cfg):

        self.commentsUrl = cfg['reddit']['commentsUrl']
        self.commentsPath = cfg['reddit']['commentsPath']
        self.rawCommentsBucket = cfg['s3']['rawCommentsBucket']
        self.cleanCommentsBucket = cfg['s3']['cleanCommentsBucket']

    def ingest(self, date):
        self.df = self.context.read.json('s3a://%s/RC_%s' \
                % (self.rawCommentsBucket, date))
        return self

    def transform(self, date):
        self.df = self.df.select('author', 'link_id', 'score', 'subreddit')
        return self

    def write(self, date):
        self.df.show()
        self.df \
            .write \
            .parquet('s3a://%s/%s' \
                % (self.cleanCommentsBucket, date), mode='overwrite')

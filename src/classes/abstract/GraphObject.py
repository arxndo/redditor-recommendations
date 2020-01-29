from Sequentiable import Sequentiable

class GraphObject(Sequentiable):

    def __init__(self, context, comments):
        self.context = context
        self.comments = comments

    def ingest(self, date):
        self.df = self.comments.dataFrame(self.context, date)
        return self

    def write(self, date):
        self.df.write.parquet('s3a://%s/nonMerged/%s'
            % (self.s3BucketName, date), mode='overwrite')

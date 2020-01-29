from Sequentiable import Sequentiable

class GraphObject(Sequentiable):

    def __init__(self, context, inBucket, outBucket):
        self.context = context
        self.comments = comments
        self.inBucket = inBucket
        self.outBucket = outBucket

    def ingest(self, date):
        self.df = self.context \
                    .read \
                    .parquet \
                    .load('s3a://%s/%s', \
                        % (self.cleanCommentsBucket, date) )
        return self

    def write(self, date):
        self.df.write.parquet('s3a://%s/nonMerged/%s' \
            % (self.s3BucketName, date), mode='overwrite')

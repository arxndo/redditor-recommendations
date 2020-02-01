from Sequentiable import Sequentiable

class GraphObject(Sequentiable):

    def __init__(self, context, inBucket, outBucket):
        self.context = context
        self.inBucket = inBucket
        self.outBucket = outBucket

    def ingest(self, date):
        self.df = self.context \
                    .read \
                    .parquet('s3a://%s/%s' \
                        % (self.inBucket, date))
        return self

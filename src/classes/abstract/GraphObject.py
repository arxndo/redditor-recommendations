import os
from Calendar import Calendar
from Sequentiable import Sequentiable

class GraphObject(Sequentiable):

    def __init__(self, context, comments, s3BucketName):
        self.context = context
        self.comments = comments
        self.s3BucketName = s3BucketName

    def ingest(self, date):
        self.df = self.comments.dataFrame(self.context, date)
        return self

    def write(self, date):
        self.df.write.parquet('s3a://%s/nonMerged/%s'
            % (self.s3BucketName, date), mode='overwrite')

        #os.system("aws s3 mv data/%s/%s s3://%s/nonMerged/%s/ --recursive" \
        #    % (self.name, date, self.s3BucketName, date))
        #os.system('rm -rf data')

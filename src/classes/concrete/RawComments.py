import os
from Sequentiable import Sequentiable

class RawComments(Sequentiable):

    def __init__(self, cfg):

        self.commentsUrl = cfg['reddit']['commentsUrl']
        self.commentsPath = cfg['reddit']['commentsPath']
        self.outBucket = cfg['s3']['rawCommentsBucket']

    def ingest(self, date):
        print('\nIngesting %s' % date)
        self.download(date)
        return self

    def transform(self, date):
        print('Transforming %s' % date)
        self.unzip(date)
        return self

    def write(self, date):
        print('Writing %s' % date)
        self.toCurrentDirectory(date)
        self.toS3(date)

    def download(self, date):
        os.system( "wget -r --no-parent -A 'RC_%s*' %s" \
            %  (date, self.commentsUrl) ) 

    def unzip(self, date):
        os.system('bzip2 -d %s/RC_%s.*' \
                % (self.commentsPath, date) )

    def toCurrentDirectory(self, date):
        os.system('mv %s/RC_%s .' \
                % (self.commentsPath, date) )

    def toS3(self, date):
        os.system("aws s3 mv RC_%s s3://%s" \
            % (date, self.outBucket ) )


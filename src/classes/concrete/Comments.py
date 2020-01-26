import os
from Sequentiable import Sequentiable

class Comments(Sequentiable):

    def __init__(self, comment_url, comment_path, s3BucketName):
        self.comment_url = comment_url
        self.s3BucketName = s3BucketName
        self.comment_path = comment_path

    def ingest(self, date):
        self.download(date)

    def transform(self, date):
        self.unzip(date)

    def write(self, date):
        self.toCurrentDirectory(date)
        self.toS3(date)

    def download(self, date):
        os.system( "wget -r --no-parent -A 'RC_%s*' %s" \
            %  (date, self.comment_url) ) 

    def unzip(self, date):
        os.system('bzip2 -d %s/RC_%s.bz2' \
                % (self.comment_path, date) )

    def toCurrentDirectory(self, date):
        os.system('mv %s/RC_%s .' \
                % (self.comment_path, date) )

    def toS3(self, date):
        os.system("aws s3 mv RC_%s s3://%s" \
            % (date, self.s3BucketName ) )

    def dataFrame(self, context, date):
        return context.read.json("s3a://%s/RC_%s" \
                    % (self.s3BucketName, date) )


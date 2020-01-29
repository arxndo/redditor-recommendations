from Sequentiable import Sequentiable

class RawComments(Sequentiable):

    def __init__(self, cfg):

        self.commentsUrl = cfg['reddit']['commentsUrl']
        self.commentsPath = cfg['reddit']['commentsPath']
        self.s3BucketName = cfg['s3']['commentsBucket']

    def ingest(self, date):
        self.download(date)
        return self

    def transform(self, date):
        self.unzip(date)
        return self

    def write(self, date):
        self.toCurrentDirectory(date)
        self.toS3(date)

    def download(self, date):
        sys.os.system( "wget -r --no-parent -A 'RC_%s*' %s" \
            %  (date, self.commentsUrl) ) 

    def unzip(self, date):
        sys.os.system('bzip2 -d %s/RC_%s.*' \
                % (self.commentsPath, date) )

    def toCurrentDirectory(self, date):
        sys.os.system('mv %s/RC_%s .' \
                % (self.commentsPath, date) )

    def toS3(self, date):
        sys.os.system("aws s3 mv RC_%s s3://%s" \
            % (date, self.s3BucketName ) )

    def dataFrame(self, context, date):
        return context.read.json("s3a://%s/RC_%s" \
                    % (self.s3BucketName, date) )


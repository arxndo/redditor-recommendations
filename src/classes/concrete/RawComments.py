import os
from Sequentiable import Sequentiable


class RawComments(Sequentiable):

    def __init__(self, cfg):

        self.commentsUrl = cfg['reddit']['commentsUrl']
        self.commentsPath = cfg['reddit']['commentsPath']
        self.outBucket = cfg['s3']['rawCommentsBucket']


    def ingest(self, date):
        """ Download data from url.
        @param date: yyyy-mm
        @return: self
        """

        print('\nIngesting %s' % date)
        os.system( "wget -r --no-parent -A 'RC_%s*' %s" \
            %  (date, self.commentsUrl) ) 
        return self


    def transform(self, date):
        """ Unzip file.
        @param date: yyyy-mm
        @return: self
        """

        print('Transforming %s' % date)
        os.system('bzip2 -d %s/RC_%s.*' \
                % (self.commentsPath, date) )
        return self


    def write(self, date):
        """ Move out of pushshift directory and
        into S3 bucket.
        @param date: yyyy-mm
        @return: none
        """

        print('Writing %s' % date)
        os.system('mv %s/RC_%s .' \
                % (self.commentsPath, date) )
        os.system("aws s3 mv RC_%s s3://%s" \
            % (date, self.outBucket ) )

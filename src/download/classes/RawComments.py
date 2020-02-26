import os
from utils.Batches import Batches
from utils.MonthlyClock import MonthlyClock

class RawComments(Batches):

    def __init__(self, cfg):
        self.commentsUrl = cfg['reddit']['commentsUrl']
        self.commentsPath = cfg['reddit']['commentsPath']
        self.outBucket = cfg['s3']['rawComments']
        self.clock = MonthlyClock()

    def ingest(self, date):

        print('\nIngesting %s' % date)
        os.system( "wget -r --no-parent -A 'RC_%s*' %s" \
            %  (date, self.commentsUrl) ) 


    def transform(self, date):

        print('Transforming %s' % date)
        os.system('bzip2 -d %s/RC_%s.*' \
                % (self.commentsPath, date) )


    def write(self, date):

        print('Writing %s' % date)
        os.system('mv %s/RC_%s .' \
                % (self.commentsPath, date) )
        os.system("aws s3 mv RC_%s s3://%s" \
            % (date, self.outBucket ) )

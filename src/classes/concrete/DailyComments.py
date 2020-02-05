from Sequentiable import Sequentiable
from Diary import Diary

class DailyComments(Sequentiable):

    def __init__(self, cfg, context):

        self.context = context
        self.inBucket = cfg['s3']['cleanCommentsBucket']
        self.outBucket = cfg['s3']['dailyCommentsBucket']

    def ingest(self, date):
        self.df = self.context.read.parquet('s3a://%s/%s' \
                % (self.inBucket, date))
        return self

    def transform(self, date):
        
        for day in Diary.monthDates(date): 
            print(day)
            nextDayUTC = Diary.toUTC(Diary.nextDate(day))

            self.df \
                .where('created_utc < %d' % nextDayUTC) \
                .show()
                #.write \
                #.parquet('s3a://%s/%s' \
                #    % (self.outBucket, day), mode='overwrite')

            self.df = self.df.where('created_utc >= %d' % nextDayUTC)

        return self

    def write(self, date):
        pass

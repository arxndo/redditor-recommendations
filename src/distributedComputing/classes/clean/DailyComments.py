from spark.classes.Batches import Batches
from utils.classes.MonthlyClock import MonthlyClock
from utils.classes.DailyClock import DailyClock

class DailyComments(Batches):
    """ Cleaned comments stored in S3 in daily batches """

    def __init__(self, cfg, context):
        self.context = context
        self.inBucket = cfg['s3']['cleanComments']
        self.outBucket = cfg['s3']['dailyComments']
        self.clock = MonthlyClock()

    def ingest(self, date):
        self.df = self.context.read.parquet('s3a://%s/%s' \
                % (self.inBucket, date))
        return self

    def transform(self, date):
        
        dailyClock = DailyClock()
        for day in dailyClock.monthDates(date): 
            nextDayUTC = dailyClock.toUTC(dailyClock.nextDate(day))

            self.df \
                .where('created_utc < %d' % nextDayUTC) \
                .write \
                .parquet('s3a://%s/%s' \
                    % (self.outBucket, day), mode='overwrite')

            self.df = self.df.where('created_utc >= %d' % nextDayUTC)

        return self

    def write(self, date):
        pass

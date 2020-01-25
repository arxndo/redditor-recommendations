from datetime import datetime
from monthdelta import monthdelta

class ScalableData:

    def __init__(self, context, comments):
        self.context = context
        self.comments = comments

    def process(self, startDate, endDate):
        for date in ScalableData.dates(startDate, endDate):
              self.ingest(date) \
                  .transform() \
                  .df
                  .write \
                  .option("header", "false") \
                  .csv('data/%s/%s' % (self.name, date))

    def merge(self):
        self.context \
            .read \
            .format('csv') \
            .load('data/%s/*.csv' % self.name) \
            .transform() \
            .df \
            .write \ 
            .option("header", "false") \
            .csv('data/%s.csv' % self.name)

    def writeAll(self):
        self.df.write \
            .option("header", "false") \
            .csv('data/%s/%s.csv' % (self.name, self.name))


    @staticmethod
    def dates(startDate, endDate):
        date = startDate

        endDatetime = datetime.strptime(endDate, "%Y-%m")

        while (datetime.strptime(date, "%Y-%m") <= endDatetime) :
            yield date

            date = (datetime.strptime(date, "%Y-%m") \
                    + monthdelta(1)) \
                     .strftime('%Y-%m')

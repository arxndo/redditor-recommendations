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
                  .write(date)

    @staticmethod
    def dates(startDate, endDate):
        date = startDate

        endDatetime = datetime.strptime(endDate, "%Y-%m")

        while (datetime.strptime(date, "%Y-%m") <= endDatetime) :
            yield date

            date = (datetime.strptime(date, "%Y-%m") \
                    + monthdelta(1)) \
                     .strftime('%Y-%m')

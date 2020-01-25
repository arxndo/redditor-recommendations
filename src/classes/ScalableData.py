from datetime import datetime
from monthdelta import monthdelta

class ScalableData:

    def __init__(context, comments):
        o.context = context
        o.comments = comments

    def process(self, startDate, endDate):
        for date in ScalableData.dates():
              self.ingest(o.context, o.comments, date) \
                  .transform() \
                  .write()

    @staticMethod
    def dates(startDate, endDate):
        date = startDate
        yield date
        while (date <= endDate):
            date = (datetime.strptime(date, %Y-%m) \
                    + monthdelta(1)) \
                     .strftime('%Y-%m')
            yield date

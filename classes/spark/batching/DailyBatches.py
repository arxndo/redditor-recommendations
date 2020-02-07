from DailyClock import DailyClock

class DailyBatches:

    def process(self, startDate, endDate):
        startDate = startDate + '-01'
        endDate =  DailyClock.endOfMonth(endDate)
        for date in DailyClock.dates(startDate, endDate):
              self.ingest(date) \
                  .transform(date) \
                  .write(date)
        return self

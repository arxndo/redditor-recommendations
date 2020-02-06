from Diary import Diary

class Quotidian:

    def process(self, startDate, endDate):
        startDate = startDate + '-01'
        endDate =  Diary.endOfMonth(endDate)
        for date in Diary.dates(startDate, endDate):
              self.ingest(date) \
                  .transform(date) \
                  .write(date)
        return self

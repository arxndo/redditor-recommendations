from Calendar import Calendar

class Data:

    def process(self, startDate, endDate):
        for date in Calendar.dates(startDate, endDate):
              self.ingest(date) \
                  .transform(date) \
                  .write(date)
        return self

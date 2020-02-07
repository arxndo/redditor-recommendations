from Batches import Batches
from MonthlyClock import MonthlyClock

class MonthlyBatches(Batches):

    def __init_(self, clock)

    def process(self, startDate, endDate):
        for date in Calendar.dates(startDate, endDate):
              self.ingest(date) \
                  .transform(date) \
                  .write(date)
        return self

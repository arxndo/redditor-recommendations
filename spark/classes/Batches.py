class Batches:

    def process(self, startDate, endDate):
        for date in self.clock.dates(startDate, endDate):
            self.ingest(date)
            self.transform(date)
            self.write(date)

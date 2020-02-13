class Batches:

    def process(self, startDate, endDate):
        for date in self.clock.dates(startDate, endDate):
            self.ingest(date) \
                .transform(date) \
                .write(date)
        return self

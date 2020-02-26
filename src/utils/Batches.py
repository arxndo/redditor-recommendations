class Batches:
    """ Abstract class whose concrete instantiations all
    process data in a temporal order defined by an instance
    of the Clock class"""

    def process(self, startDate, endDate):
        for date in self.clock.dates(startDate, endDate):
            self.ingest(date)
            self.transform(date)
            self.write(date)

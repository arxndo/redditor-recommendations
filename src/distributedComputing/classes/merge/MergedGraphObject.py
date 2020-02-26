
class MergedGraphObject:
 
    def process(self, startDate, endDate):
        self.ingest(startDate, endDate) \
            .transform() \
            .write(startDate, endDate)


    def ingest(self, startDate, endDate):

        paths = self.clock.s3paths(self.inBucket, startDate, endDate)
        self.df = self.context.read.parquet(*paths)
        return self


    def transform(self):
        pass

    def write(self, startDate, endDate):
        self.df \
        .repartition(1) \
        .write \
        .option('header', 'false') \
        .mode('overwrite') \
        .csv('s3a://%s/%s_%s_%s' \
            % (self.outBucket, self.name, startDate, endDate))
        return self


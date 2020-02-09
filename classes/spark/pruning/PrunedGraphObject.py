class PrunedGraphObject:
 
    def process(self, startDate, endDate):
        self.ingest(startDate, endDate) \
            .transform() \
            .write(startDate, endDate)


    def ingest(self, startDate, endDate):
        self.df \
            .read \
            .option('header', 'false') \
            .csv('s3a://%s/%s_%s_%s' \
                % (self.inBucket, self.inName, startDate, endDate))

        return self


    def transform(self):
        pass

    def write(self, startDate, endDate):
        pass

from MonthlyBatches import MonthlyBatches

class MergedGraphObject:
 
    def __init__(self, context, cfg):
        self.context = context
        self.inBucket = cfg['s3']['nodesBucket']
        self.outBucket = cfg['s3']['mergedNodesBucket']
        self.truncation = cfg['tuning']['truncation']

    def process(self, startDate, endDate):
        self.ingest(startDate, endDate) \
            .transform() \
            .write(startDate, endDate)


    def ingest(self, startDate, endDate):

        paths = MonthlyClock().s3paths(self.inBucket, startDate, endDate)
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
        .csv('s3a://%s/%s_%s' \
            % (self.outBucket, startDate, endDate))
        return self


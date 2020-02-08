class GraphObject:

    def __init__(self, context, inBucket, outBucket):
        self.context = context
        self.inBucket = inBucket
        self.outBucket = outBucket

    def ingest(self, date):
        self.df = self.context \
                    .read \
                    .parquet('s3a://%s/%s' \
                        % (self.inBucket, date))
        return self

    def write(self, date):
        self.df \
            .repartition(1) \
            .write \
            .parquet('s3a://%s/%s' \
                % (self.outBucket, date), mode='overwrite')

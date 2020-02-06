
class EdgeHistogram:
    """ Creates histogram of edge weights"""
 
    def __init__(self, context, cfg):
        self.context = context
        self.inBucket = cfg['s3']['mergedEdgesBucket']
        self.outBucket = cfg['s3']['analysisBucket']


    def process(self, startDate, endDate):
        """ Histogram of edges from startDate to endDate"""
        self.ingest(startDate, endDate) \
            .transform() \
            .write(startDate, endDate)


    def ingest(self, startDate, endDate):
        """ Read merged edges """

        self.df = self.context.read.parquet('s3a://%s/%s_%s' \
                % (self.inBucket, startDate, endDate))
        return self


    def transform(self):
        """ Create histogram """

        self.df = self.df.select('weight') \
                    .orderBy('weight')
        return self


    def write(self, startDate, endDate):
        """ Save plot to s3 """

        self.df.write.csv('s3://%s/weight_%s_%s' \
             % (self.outBucket, startDate, endDate) )



class MergedEdgeAnalysis:
    """ Analysis for pruning"""
 
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

        self.df = self.df.select('weight')

        print('%d, %d' % (0, self.df.count()))
        for i in range(1,100):
            self.df = self.df.where('weight > %d' % i)
            print('%d, %d' % (i, self.df.count()))
        return self


    def write(self, startDate, endDate):
        """ Save plot to s3 """
        pass

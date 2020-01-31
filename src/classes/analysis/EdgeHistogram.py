
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

        self.df.read.parquet('s3a://%s/%s_%s' \
                % (self.inBucket, startDate, endDate))
        return self


    def transform(self):
        """ Create histogram """

        self.df.select('weight')
        return self


    def write(self, startDate, endDate):
        """ Save plot to s3 """

        self.df.show(20)
        self.df \
            .repartition(1) \
            .write.format('com.databricks.spark.csv') \
            .save('weight_%s_%s' % (startDate, endDate))


        #fig = self.hist.get_figure()

        #fig.savefig('histogram.png')

        #fig.savefig('s3a://%s/%s_%s' \
        #        % (self.outBucket, startDate, endDate))


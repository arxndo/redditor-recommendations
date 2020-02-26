from Batches import Batches
from MonthlyClock import MonthlyClock

class GraphObject(Batches):
    """ Abstract class whose instantiations load data from 
    S3 parquet files into a spark data frame, transform the
    data in some way, and then write the results back into 
    separate S3 parquet files """

    def ingest(self, date):
        self.df = self.context \
                    .read \
                    .parquet('s3a://%s/%s' \
                        % (self.inBucket, date))
        return self

    def write(self, date):
        self.df \
            .repartition(self.partitions) \
            .write \
            .parquet('s3a://%s/%s' \
                % (self.outBucket, date), mode='overwrite')

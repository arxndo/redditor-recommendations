from Batches import Batches
from MonthlyClock import MonthlyClock

class GraphObject(Batches):

    def __init__(self):
        super().__init__(MonthlyClock())

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

from pyspark.sql import functions as F
from MergedGraphObject import MergedGraphObject

class MergedNodes(MergedGraphObject):
 
    def __init__(self, context, cfg):
        self.context = context
        self.inBucket = cfg['s3']['nodesBucket']
        self.outBucket = cfg['s3']['mergedNodesBucket']

    def transform(self):
        self.df = self.df \
            .groupBy(self.label) \
            .agg( F.sum('score').alias('score'))
        return self


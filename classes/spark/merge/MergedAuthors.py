from pyspark.sql import functions as F
from MergedGraphObject import MergedGraphObject

class MergedAuthors(MergedNodes):
 
    def __init__(self, context, cfg):
        self.context = context
        self.inBucket = cfg['s3']['nodesBucket']
        self.outBucket = cfg['s3']['mergedNodesBucket']
        self.label = 'author'


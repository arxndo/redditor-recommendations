from pyspark.sql import functions as F
from MergedNodes import MergedNodes
from MonthlyClock import MonthlyClock

class MergedAuthors(MergedNodes):
 
    def __init__(self, cfg, context):
        self.context = context
        self.inBucket = cfg['s3']['authors']
        self.outBucket = cfg['s3']['merged']
        self.clock = MonthlyClock()
        self.label = 'author'
        self.valueName = 'score'
        self.name = 'authors'

from AuthorAuthorEdges import AuthorAuthorEdges
from DailyClock import DailyClock

class DailyAuthorAuthorEdges(AuthorAuthorEdges):
 
    def __init__(self, cfg, context):
        self.context = context
        self.inBucket = cfg['s3']['dailyComments']
        self.outBucket = cfg['s3']['dailyEdges']
        self.truncation = cfg['tuning']['truncation']
        self.partitions = cfg['tuning']['edgePartitions']
        self.clock = DailyClock()

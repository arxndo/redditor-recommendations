from Edges import Edges
from AuthorEdges import AuthorEdges
from MonthlyClock import MonthlyClock

class DailyAuthorAuthorEdges(AuthorAuthorEdges):
 
    def __init__(self, cfg, context):
        self.context = context
        self.inBucket = cfg['s3']['dailyCommentsBucket'], \
        self.inBucket = cfg['s3']['dailyEdgesBucket'])
        self.truncation = cfg['tuning']['truncation']
        self.partitions = cfg['tuning']['edgePartitions']
        self.clock = MonthlyClock()

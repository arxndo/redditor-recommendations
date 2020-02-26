from AuthorAuthorEdges import AuthorAuthorEdges
from MonthlyClock import MonthlyClock

class MonthlyAuthorAuthorEdges(AuthorAuthorEdges):
    """ Deprecated: Directly edge between authors, 
    computed by determining number of common urls to which 
    any pair of authors has posted comments to in a given month.
    This is intractable for very large numbers of authors."""
 
    def __init__(self, cfg, context):
        self.context = context
        self.inBucket = cfg['s3']['cleanComments']
        self.outBucket = cfg['s3']['dailyEdges']
        self.truncation = cfg['tuning']['truncation']
        self.partitions = cfg['tuning']['edgePartitions']
        self.clock = MonthlyClock()

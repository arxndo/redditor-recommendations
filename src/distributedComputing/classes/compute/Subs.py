from MonthlyClock import MonthlyClock
from Nodes import Nodes

class Subs(Nodes):
    """ Subreddits """
 
    def __init__(self, cfg, context):
        self.context = context
        self.inBucket = cfg['s3']['cleanComments']
        self.outBucket = cfg['s3']['subreddits']
        self.label = 'subreddit'
        self.valueName = 'score'
        self.partitions = cfg['tuning']['nodePartitions']
        self.clock = MonthlyClock()
        

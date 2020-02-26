from MergedNodes import MergedNodes
from MonthlyClock import MonthlyClock

class MergedSubs(MergedNodes):
    """ Merges subreddits """
 
    def __init__(self, cfg, context):
        self.context = context
        self.inBucket = cfg['s3']['subreddits']
        self.outBucket = cfg['s3']['merged']
        self.clock = MonthlyClock()
        self.label = 'subreddit'
        self.valueName = 'score'
        self.name = 'subs'

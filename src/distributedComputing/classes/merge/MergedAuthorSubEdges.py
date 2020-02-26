from MergedEdges import MergedEdges
from MonthlyClock import MonthlyClock

class MergedAuthorSubEdges(MergedEdges):
    """ Merges author-to-subreddit edges """
 
    def __init__(self, cfg, context):
        self.context = context
        self.inBucket = cfg['s3']['relationships']
        self.outBucket = cfg['s3']['merged']
        self.clock = MonthlyClock()
        self.label1 = 'author'
        self.label2 = 'subreddit'
        self.valueName = 'score'
        self.name = 'author-sub'

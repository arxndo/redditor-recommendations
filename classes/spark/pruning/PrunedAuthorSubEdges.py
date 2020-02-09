from PrunedEdges import PrunedEdges

class PrunedAuthorSubEdges(PrunedEdges):
 
    def __init__(self, cfg, context):
        self.context = context
        self.inBucket = cfg['s3']['merged']
        self.outBucket = cfg['s3']['merged']
        self.label1 = 'author'
        self.label2 = 'subreddit'
        self.valueName = 'score'
        self.truncation = cfg['tuning']['truncation']
        self.inName = 'author-sub'
        self.outName = 'prune%d-author-sub' % self.truncation

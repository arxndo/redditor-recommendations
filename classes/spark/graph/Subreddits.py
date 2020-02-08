from Nodes import Nodes

class Subreddits(Nodes):
 
    def __init__(self, cfg, context):
        self.context = context
        self.inBucket = cfg['s3']['cleanCommentsBucket']
        self.outbucket = cfg['s3']['subredditsBucket']
        self.label = 'subreddits'

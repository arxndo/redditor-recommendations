from Nodes import Nodes

class Subreddits(Nodes):
 
    def __init__(self, cfg, context):
        super().__init__(context, \
                        cfg['s3']['cleanCommentsBucket'], \
                        cfg['s3']['subredditsBucket'])
        self.label = 'subreddit'

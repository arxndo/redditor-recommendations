from MergedGraphObject import MergedGraphObject

class MergedSubreddits(MergedNodes):
 
    def __init__(self, context, cfg):
        self.context = context
        self.inBucket = cfg['s3']['subredditsBucket']
        self.outBucket = cfg['s3']['mergedSubredditsBucket']
        self.label = 'subreddit'

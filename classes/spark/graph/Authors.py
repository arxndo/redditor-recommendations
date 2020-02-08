from MonthlyClock import MonthlyClock
from Nodes import Nodes

class Authors(Nodes):
 
    def __init__(self, cfg, context):
        self.context = context
        self.inBucket = cfg['s3']['cleanCommentsBucket']
        self.outBucket = cfg['s3']['authorsBucket']
        self.label = 'author'
        self.valueName = 'score'
        self.partitions = cfg['tuning']['nodePartitions']
        self.clock = MonthlyClock()

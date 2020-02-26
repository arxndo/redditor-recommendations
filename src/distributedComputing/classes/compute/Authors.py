from MonthlyClock import MonthlyClock
from Nodes import Nodes

class Authors(Nodes):
    """ The authors of comments """
 
    def __init__(self, cfg, context):
        self.context = context
        self.inBucket = cfg['s3']['cleanComments']
        self.outBucket = cfg['s3']['authors']
        self.label = 'author'
        self.valueName = 'score'
        self.partitions = cfg['tuning']['nodePartitions']
        self.clock = MonthlyClock()

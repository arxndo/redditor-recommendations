from Edges import Edges

class DailyEdges(Edges, Quotidian):
 
    def __init__(self, cfg, context):
        super().__init__(context, \
                        cfg['s3']['cleanCommentsBucket'], \
                        cfg['s3']['dailyEdgesBucket'])
        self.truncation = cfg['tuning']['truncation']
        self.partitions = cfg['tuning']['edgePartitions']


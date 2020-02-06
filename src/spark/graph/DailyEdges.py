from Edges import Edges
from Quotidian import Quotidian

class DailyEdges(Edges, Quotidian):
 
    def __init__(self, cfg, context):
        super().__init__(cfg, context, \
                        cfg['s3']['dailyCommentsBucket'], \
                        cfg['s3']['dailyEdgesBucket'])

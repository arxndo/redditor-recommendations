from Edges import Edges
from DailyBatches import DailyBatches

class DailyEdges(Edges, DailyBatches):
 
    def __init__(self, cfg, context):
        super().__init__(cfg, context, \
                        cfg['s3']['dailyCommentsBucket'], \
                        cfg['s3']['dailyEdgesBucket'])

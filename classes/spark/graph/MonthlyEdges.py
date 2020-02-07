from Edges import Edges

class MonthlyEdges(GraphObject, Sequentiable):
 
    def __init__(self, cfg, context):
        super().__init__(context, \
                        cfg['s3']['cleanCommentsBucket'], \
                        cfg['s3']['edgesBucket'])

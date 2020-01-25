from ScalableData import ScalableData

class Scores(ScalableData):
 
    name = 'scores'

    def ingest(self, date):
        self.df = self.comments.dataFrame(self.context, date) 
        return self

    def ingestAll(self):
        self.df = self.context.read \
                      .format('csv') \
                      .load('data/scores/*.csv')

    def transform(self):
        self.df = self.df.groupBy("author") \
                         .agg( {"score" : "sum"} )
        return self

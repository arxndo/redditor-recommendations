from ScalableData import ScalableData

class AuthorScores(ScalableData):
 
    def ingest(self, date):
        self.df = self.comments.dataFrame(self.context, date) 
        return self

    def transform(self):
        self.df = self.df.groupBy("author") \
                         .agg( {"score" : "sum"} )
        return self

    def write(self, date):
        self.df.show(10)
        self.df.write \
            .option("header", "false") \
            .csv('data/authorScores/%s' % date)


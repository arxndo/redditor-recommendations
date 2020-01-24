from ScalableData import ScalableData

class AuthorScores(ScalableData):
 
    def ingest(self, date):
        self.df = comments.dataFrame(o.context, date) 
        return self

    def transform(self):
        self.df = self.df.groupBy("author") \
                         .agg( {"score" : "sum"} ) \
        return self

    def write(self):
        self.df.show(10)
        self.df.write. \
            .option("header", "false") \
            .csv('authorScores')


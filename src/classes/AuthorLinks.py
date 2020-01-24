from pyspark.sql import functions as F
from ScalableData import ScalableData

class AuthorLinks(ScalableData):
 
    def ingest(self, date):
        self.df = comments.dataFrame(o.context, calendar) 
        return self

    def collectLinks(self):
        self.df = self.df.groupBy("author") \
                      .agg(F.collect_set("link_id" ))
        return self

    def write(self):
        self.df.show(10)
        #self.df.write.option("header", "true").csv('authorScores')


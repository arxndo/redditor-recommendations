from pyspark.sql import functions as F
from Sequenced import Sequenced

class Links(Sequenced):
 
    def ingest(self, date):
        self.df = self.comments.frame(self.context, calendar) 
        return self

    def collectLinks(self):
        self.df = self.df.groupBy("author") \
                      .agg(F.collect_set("link_id" ))
        return self

    def write(self, date):
        self.df.show(10)
        #self.df.write.option("header", "true").csv('authorScores')


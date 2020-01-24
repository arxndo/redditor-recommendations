import os
from pyspark.sql import functions as F

class AuthorLinks:
 
    def loadComments(self, context, comments, calendar):
        self.df = comments.dataFrame(context, calendar) 
        return self

    def collectLinks(self):
        self.df = self.df.groupBy("author") \
                      .agg(F.collect_set("link_id" ))
        return self

    def write(self):
        self.df.show(10)
        #self.df.write.option("header", "true").csv('authorScores')


import os
from pyspark.sql import functions as F

class AuthorScores:
 
    def loadComments(self, spark, comments, calendar):
        self.df = comments.dataFrame(comments, calendar) 

    def addScores(self):
        self.df = self.groupBy("author") \
                      .agg( {"score" : "sum"} ) \
                      .withColumnRename("sum(score)", "score")

    def write(self):
        self.show(10)
        self.df.write.option("header", "true").csv('authorScores')


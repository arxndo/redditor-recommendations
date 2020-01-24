import os

class Authors:
 
    def writeToCSV(self, spark, comments, calendar):
        df = comments.dataFrame(spark, calendar)
        df.write.csv('data')

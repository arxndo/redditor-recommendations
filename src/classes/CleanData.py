import os

class CleanData:

    def writeAuthors(self, comments, calendar):

    def writeRelationships(self, comments, calendar):

    def downloadAll(self, calendar): 
        for month, year in calendar.dates():
            self.download(month, year)
            self.unzip(month, year)
            self.moveToCurrentDirectory(month, year)
            self.moveToS3(month, year)

    def countAll(self, spark, calendar):
        count = 0;
        for month, year in calendar.dates():
            count += self.count(spark, month, year)
        return count

    def count(self, spark, month, year):
        df = self.dataFrame(spark, month, year)
        return df.count()

    def countAuthors(self, spark, month, year):
        df = self.dataFrame(spark, month, year)
        return df.select("author").distinct().count()        

    def dataFrame(self, spark, month, year):
        return spark.read.json("s3a://%s/RC_%d-%.2d" \
                % (self.s3BucketName, year, month) )

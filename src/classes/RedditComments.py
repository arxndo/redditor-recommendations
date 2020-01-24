import os

class RedditComments:

    def __init__(self, comment_url, comment_path, s3BucketName):
        self.comment_url = comment_url
        self.s3BucketName = s3BucketName
        self.comment_path = comment_path

    def downloadAll(self, calendar): 
        for month, year in calendar.dates():
            self.download(month, year)
            self.unzip(month, year)
            self.moveToCurrentDirectory(month, year)
            self.moveToS3(month, year)

    def download(self, month, year):
        os.system( "wget -r --no-parent -A 'RC_%d-%.2d*' %s" \
            %  (year, month, self.comment_url) ) 

    def unzip(self, month, year):
        os.system('bzip2 -d %s/RC_%d-%.2d.bz2' \
                % (self.comment_path, year, month) )

    def moveToCurrentDirectory(self, month, year):
        os.system('mv %s/RC_%d-%.2d .' \
                % (self.comment_path, year, month) )

    def moveToS3(self, month, year):
        os.system("aws s3 mv RC_%d-%.2d s3://%s" \
            % (year, month, self.s3BucketName ) )

    def countAllAuthors(self, spark, calendar):
        authorCount = 0;
        for month, year in calendar.dates():
            authorCount += self.countAuthors(spark, month, year) 
        return authorCount

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

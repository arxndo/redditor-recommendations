import os

class Comments:

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

    def count(self, spark, calendar):
        df = self.dataFrame(spark, calendar)
        return df.count()

    def countAuthors(self, spark, calendar):
        df = self.dataFrame(spark, calendar)
        return df.select("id").distinct().count()        

    def dataFrame(self, spark, calendar):
        counter = 1
        for month, year in calendar.dates():
            newDF = spark.read.json("s3a://%s/RC_%d-%.2d" \
                    % (self.s3BucketName, year, month) ) 
            newDF.printSchema()

            newDF = newDF.select("id", "parent_id", "score", "subreddit_id" )

            if counter == 1:
                df = newDF
            else:
                df = df.union(newDF)
            counter += 1
        return df






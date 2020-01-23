import os

class RedditComments:

    def __init__(o, comment_url, comment_path, s3BucketName):
        o.comment_url = comment_url
        o.s3BucketName = s3BucketName
        o.comment_path = comment_path

    def downloadAll(o, calendar): 
        for month, year in calendar.dates():
            o.download(month, year)
            o.unzip(month, year)
            o.moveToCurrentDirectory(month, year)
            o.moveToS3(month, year)

    def download(o, month, year):
        os.system( "wget -r --no-parent -A 'RC_%d-%.2d*' %s" \
            %  (year, month, o.comment_url) ) 

    def unzip(o, month, year):
        os.system('bzip2 -d %s/RC_%d-%.2d.bz2' \
                % (o.comment_path, year, month) )

    def moveToCurrentDirectory(o, month, year):
        os.system('mv %s/RC_%d-%.2d .' \
                % (o.comment_path, year, month) )

    def moveToS3(o, month, year):
        os.system("aws s3 mv RC_%d-%.2d s3://%s" \
            % (year, month, o.s3BucketName ) )

    def clean(o, sparkS3, month, year):
        spark = sparkS3.spark
        #df = spark.read.json("RC_%d-%.2d" \
                #% (year, month) )
        df = spark.read.json("s3a://%s/RC_%d-%.2d" \
                % (o.s3BucketName, year, month) )
        df.show()

    def show(o, month, year):
        os.system("head -10 RC_%d-%.2d" \
            % (year, month) )

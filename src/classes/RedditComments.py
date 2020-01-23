import os

class RedditComments:

    def __init__(o, comment_url, s3BucketName):
        o.comment_url = comment_url
        o.s3BucketName = s3BucketName

    def downloadBatches(o, calendar): 
        for month, year in calendar.dates():
            os.system("mk downloads")
            o.downloadBatch(month, year)
            #o.moveBatchToS3()
            #os.system("rm -rf downloads")

    def downloadBatch(o, month, year):
        os.system( "wget -r --no-parent -A 'RC_%d-%.2d*' %s -P downloads" \
            %  (year, month, o.comment_url) ) 

    def moveBatchToS3(o):
        os.system("aws s3 mv downloads s3://%s --recursive" \
            % o.s3BucketName )


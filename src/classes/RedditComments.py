import os

class RedditComments:

    def __init__(o, comment_url, s3BucketName):
        o.comment_url = comment_url
        o.s3BucketName = s3BucketName

    def downloadBatches(o, startMonth, startYear, endMonth, endYear): 
        year = startYear
        month = startMonth
        while RedditComments.withinBounds(year, month, endYear, endMonth):
            RedditComments.makeDownloadsDirectory()
            o.downloadBatch(month, year)
            #o.moveBatchToS3()
            RedditComments.removeDownloadsDirectory()
            month, year = RedditComments.advanceTime(month, year)

    def downloadBatch(o, month, year):
        os.system( "wget -r --no-parent -A 'RC_%d-%.2d*' %s -P downloads" \
            %  (year, month, o.comment_url) ) 

    def moveBatchToS3(o):
        os.system("aws s3 mv downloads s3://%s --recursive" \
            % o.s3BucketName )

    @staticmethod
    def advanceTime(month, year):
        if month < 12:
            month += 1
        else:
            month = 1
            year += 1
        return month, year

    @staticmethod
    def withinBounds(year, month, endYear, endMonth):
        return (year < endYear) | ( (year == endYear) & (month <= endMonth) )

    @staticmethod
    def makeDownloadsDirectory():
        os.system("mk downloads")

    @staticmethod
    def removeDownloadsDirectory():
        os.system("rm -rf downloads")


from pyspark.sql import SparkSession
#import boto3

class SparkS3:
    def __init__(o, appName, bucketName):
        o.spark = SparkSession \
                    .builder \
                    .appName(appName) \
                    .getOrCreate()

#        o.s3 = boto3.resource('s3')


    def jsonToDataFrame(o, bucketName, fileName):
        return spark.read.json("s3a://%s/%s" \
                % (bucketName, fileName) )

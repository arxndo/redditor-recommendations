from pyspark.sql import SparkSession

class SparkSuite:
    def __init__(o, appName):
        o.appName = appName

    def spark(o):
        return SparkSession \
                .builder \
                .appName(o.appName) \
                .getOrCreate()



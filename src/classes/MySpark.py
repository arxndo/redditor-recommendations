from pyspark.sql import SparkSession

class MySpark:
    
    def spark(self):
        return SparkSession \
                    .builder \
                    .appName("romeosSpark") \
                    .getOrCreate()

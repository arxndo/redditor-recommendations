from pyspark.sql import SparkSession
from pyspark.sql import HiveContext

class MyContext:
    
    def context(self):
        sc = SparkSession \
       	     .builder \
             .appName("romeosSpark") \
             .getOrCreate()

        hiveContext = HiveContext(sc)
        return hiveContext

from pyspark.sql import SparkSession
from pyspark.sql import HiveContext

class MyContext:
    
    @staticmethod
    def context(cfg):
        sparkContext = SparkSession \
       	          .builder \
                  .appName(cfg['spark']['appName']) \
                  .master(cfg['spark']['master']) \
                  .getOrCreate() \
                  .sparkContext

        hiveContext = HiveContext(sparkContext)

        return hiveContext

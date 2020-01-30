from pyspark.sql import SparkSession
from pyspark.sql import HiveContext

class MyContext:
    
    @staticmethod
    def context(cfg, appName):
        sparkContext = SparkSession \
       	          .builder \
                  .appName(appName) \
                  .master(cfg['spark']['master']) \
                  .config('spark.executor.memory', '2G') \
                  .getOrCreate() \
                  .sparkContext

        hiveContext = HiveContext(sparkContext)

        return hiveContext

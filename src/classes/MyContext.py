from pyspark.sql import SparkSession
#from pyspark.sql import SQLContext
from pyspark.sql import HiveContext

class MyContext:
    
    def context(self):
        session = SparkSession \
       	          .builder \
                  .appName("romeosSpark") \
                  .getOrCreate()


        sparkContext = session.sparkContext
       #     .addFile('src/classes/*.py')

        hiveContext = HiveContext(sparkContext)
        return hiveContext

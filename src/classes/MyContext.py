from pyspark.sql import SparkSession
#from pyspark.sql import SQLContext
from pyspark.sql import HiveContext

class MyContext:
    
    def context(self):
        session = SparkSession \
       	          .builder \
                  .appName("romeosSpark") \
                  .master('spark://10.0.0.11:7077') \
                  .getOrCreate()


        sparkContext = session.sparkContext
            #.addFile('src/scripts/computeEdges') \
            #.addFile('src/classes/concrete/Edges.py') \
            #.addFile('src/classes/concrete/Comments.py') \
            #.addFile('src/classes/Calendar.py') \
            #.addFile('src/classes/MyContext')


        hiveContext = HiveContext(sparkContext)


        return hiveContext

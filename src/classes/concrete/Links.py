from pyspark.sql import functions as F
from RawInput import RawInput
from Sequentiable import Sequentiable

class Links(RawInput, Sequentiable):
 
    name = 'links'
    nodeName = 'author'

    def __init__(self, context, comments):
        self.context = context
        self.comments = comments

    def transform(self, date):
        self.df = self.df.groupBy("author") \
                      .agg(F.collect_set("link_id" )) \
                      .withColumnRenamed('collect_set(link_id)', 'link_ids')

        df1 = self.df.withColumnRenamed('author', 'author_1') \
                     .withColumnRenamed('link_ids', 'link_ids_1')

        df2 = self.df.withColumnRenamed('author', 'author_2') \
                     .withColumnRenamed('link_ids', 'link_ids_2')

        self.df = df1.crossJoin(df2) \
                     .where(df1.author_1 > df2.author_2)

        return self

    def write(self, date):
        self.df.show(10)
        #self.df.write.option("header", "true").csv('authorScores')


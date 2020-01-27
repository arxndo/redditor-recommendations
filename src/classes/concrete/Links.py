from pyspark.sql import functions as F
from RawInput import RawInput
from Sequentiable import Sequentiable

class Edges(GraphObject):
 
    name = 'edges'

    def transform(self, date):
        self.df = self.df.where('author != "[deleted]"') \
                      .groupBy("author") \
                      .agg(F.collect_set("link_id" )) \
                      .withColumnRenamed('collect_set(link_id)', 'link_ids')

        df1 = self.df.withColumnRenamed('author', 'author_1') \
                     .withColumnRenamed('link_ids', 'link_ids_1')

        df2 = self.df.withColumnRenamed('author', 'author_2') \
                     .withColumnRenamed('link_ids', 'link_ids_2')

        self.df = df1.crossJoin(df2) \
                 .where(df1.author_1 < df2.author_2) \
                 .select('author_1', \
                       'author_2', \
                       F.size(F.array_intersect('link_ids_1', 'link_ids_2'))) \
                 .withColumnRenamed('size(array_intersect(link_ids_1, link_ids_2))', \
                                    'weight') \
                 .where('weight > 0')

        return self



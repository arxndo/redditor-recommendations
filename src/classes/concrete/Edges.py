from pyspark.sql import functions as F
from Sequentiable import Sequentiable
from GraphObject import GraphObject
from Calendar import Calendar
import os

class Edges(GraphObject):
 
    name = 'edges'

    def __init__(self, comments, context, cfg):
        self.s3BucketName = cfg['s3']['edgesBucket']
        super().__init__(comments, context)

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
                 .where('weight > 0') \


        return self


    def merge(self, startDate, endDate):

        df = self.context \
            .read \
            .parquet \
            .load(Calendar.paths(self.name, startDate, endDate)) \
            .groupBy('author_1', 'author_2') \
            .agg( {'weight' : 'sum'} ) \
            .withColumnRenamed('sum(weight)', 'weight') \
            .sort(F.desc('weight')) \
            .write \
            .parquet('data/%s/%s_%s' % (self.name, startDate, endDate))

        
        os.system('aws s3 mv data/%s/%s_%s s3://%s/merged/%s_%s/ --recursive' \
            % (self.name, startDate, endDate, self.s3BucketName, startDate, endDate))


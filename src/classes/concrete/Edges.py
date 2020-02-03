from pyspark.sql import functions as F
from GraphObject import GraphObject

class Edges(GraphObject):
 
    def __init__(self, cfg, context):
        super().__init__(context, \
                        cfg['s3']['cleanCommentsBucket'], \
                        cfg['s3']['edgesBucket'])
        self.truncation = cfg['tuning']['truncation']
        self.partitions = cfg['tuning']['edgePartitions']

    def transform(self, date):
        self.df = self.df \
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
                 .where('weight > %d' % self.truncation)

        return self

    def write(self, date):
        n = self.partitions
        self.df = self.df.repartition(n)
        self.df \
            .write \
            .parquet('s3a://%s/%s' \
                % (self.outBucket, date), mode='overwrite')

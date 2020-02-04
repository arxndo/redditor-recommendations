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
                      .groupBy('author') \
                      .agg(F.collect_set("link_id" ).alias('link_ids')) \
                      .repartition('author')

        self.df = self.df.alias('df1') \
                .join(self.df.alias('df2')) \
                .where('df1.author < df2.author') \
                .select(F.col('df1.author').alias('author_1'), \
                    F.col('df2.author').alias('author_2'), \
                    F.size(F.array_intersect('df1.link_ids',
                                             'df2.link_ids')) \
                        .alias('weight')) \
                .where('weight > %d' % self.truncation)

        return self

    def write(self, date):
        n = self.partitions
        self.df = self.df.repartition(n)
        self.df \
            .write \
            .parquet('s3a://%s/%s' \
                % (self.outBucket, date), mode='overwrite')

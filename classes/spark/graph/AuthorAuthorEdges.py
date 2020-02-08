from pyspark.sql import functions as F
from GraphObject import GraphObject

class AuthorAuthorEdges(GraphObject):
 
    def __init__(self, cfg, context):
        self.context = context
        self.inBucket = cfg['s3']['cleanCommentsBucket']
        self.outBucket = cfg['s3']['dailyEdgesBucket']
        self.truncation = cfg['tuning']['truncation']
        self.partitions = cfg['tuning']['edgePartitions']
        self.clock = MonthlyClock()

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

from pyspark.sql import functions as F
from GraphObject import GraphObject

class AuthorAuthorEdges(GraphObject):
    """ Deprecated: Directly edge between authors, 
    computed by determining number of common urls to which 
    any pair of authors has posted comments to. This is intractable
    for very large numbers of authors."""

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

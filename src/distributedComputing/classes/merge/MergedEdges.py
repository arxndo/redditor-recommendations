from pyspark.sql import functions as F
from MergedGraphObject import MergedGraphObject

class MergedEdges(MergedGraphObject):
    """ Merges edges (ie. author-to-subreddit edges """
 
    def transform(self):
        self.df = self.df \
            .groupBy(self.label1, self.label2) \
            .agg(F.sum(self.valueName).alias(self.valueName))
        return self

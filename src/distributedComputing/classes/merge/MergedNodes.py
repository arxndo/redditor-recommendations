from pyspark.sql import functions as F
from MergedGraphObject import MergedGraphObject

class MergedNodes(MergedGraphObject):
    """ Merges nodes (ie. authors and subreddits) """
 
    def transform(self):
        self.df = self.df \
            .groupBy(self.label) \
            .agg( F.sum(self.valueName).alias(self.valueName))
        return self


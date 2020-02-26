from pyspark.sql import functions as F
from GraphObject import GraphObject

class Nodes(GraphObject):
    """ A Graph Object that transforms data by aggregating values
    within a batch corresponding to a given data
    (eg. authors and subreddits) """
 
    def transform(self, date):
        self.df = self.df \
                .select(self.label, self.valueName) \
                .groupBy(self.label) \
                .agg(F.sum(self.valueName).alias(self.valueName))
        return self

from pyspark.sql import functions as F
from GraphObject import GraphObject

class Nodes(GraphObject):
 
    def transform(self, date):
        self.df = self.df \
                .select(self.label, 'score') \
                .groupBy(self.label) \
                .agg(F.sum('score').alias('score'))
        return self

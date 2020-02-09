from pyspark.sql import functions as F
from PrunedGraphObject import PrunedGraphObject

class PrunedEdges(PrunedGraphObject):
 
    def transform(self):
        for i in range(1,10):
            print(self.df.where('_3 > %d' % i))

        #self.df = self.df \
        #              .where(self.valueName > self.truncation)
        return self

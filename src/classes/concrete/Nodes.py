from GraphObject import GraphObject
from Sequentiable import Sequentiable

class Nodes(GraphObject, Sequentiable):
 
    name = 'nodes'

    def transform(self, date):
        self.df = self.df.groupBy('author') \
                         .agg( {'score' : 'sum'} ) \
                         .withColumnRenamed('sum(score)', 'score')
        return self


    def merge(self, startDate, endDate):

        df = self.context \
            .read \
            .format('csv') \
            .load(self.paths(startDate, endDate)) \
            .groupBy('author') \
            .agg( {'score' : 'sum'} ) \
            .withColumnRenamed('sum(score)', 'score') \
            .write \
            .option('header', 'true') \
            .csv('data/%s/%s_%s' % (self.name, startDate, endDate))

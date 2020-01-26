from Data import Data
from Mergeable import Mergeable

class Scores(Data, Mergeable):
 
    name = 'scores'
    column1Name = 'author'
    column2Name = 'score'

    def __init__(self, context, comments):
        self.context = context
        self.comments = comments

    def ingest(self, date):
        self.df = self.comments.dataFrame(self.context, date) 
        return self

    def transform(self, date):
        self.df = self.df.groupBy(self.column1Name) \
                         .agg( {self.column2Name : 'sum'} )
        return self

    def write(self, date):
        self.df \
            .write \
            .option('header', 'true') \
            .csv('data/%s/%s' % (self.name, date))

from Mergeable import Mergeable
from Sequentiable import Sequentiable
from RawInput import RawInput

class Scores(RawInput, Sequentiable, Mergeable):
 
    name = 'scores'
    column1Name = 'author'
    column2Name = 'score'

    def __init__(self, context, comments):
        self.context = context
        self.comments = comments

    def transform(self, date):
        self.df = self.df.groupBy(self.column1Name) \
                         .agg( {self.column2Name : 'sum'} )
        return self

    def write(self, date):
        self.df \
            .write \
            .option('header', 'true') \
            .csv('data/%s/%s' % (self.name, date))

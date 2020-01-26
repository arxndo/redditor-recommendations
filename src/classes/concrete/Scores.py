from Mergeable import Mergeable
from Sequentiable import Sequentiable
from RawInput import RawInput

class Scores(RawInput, Sequentiable, Mergeable):
 
    name = 'scores'
    nodeName = 'author'
    weightName = 'score'

    def __init__(self, context, comments):
        self.context = context
        self.comments = comments

    def transform(self, date):
        self.df = self.df.groupBy(self.nodeName) \
                         .agg( {'%s' % self.weightName : 'sum'} )
        return self

    def write(self, date):
        self.df \
            .write \
            .csv('data/%s/%s' % (self.name, date))

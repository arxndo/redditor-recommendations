from Calendar import Calendar
from Sequentiable import Sequentiable

class GraphObject(Sequentiable):

    def __init__(self, context, comments):
        self.context = context
        self.comments = comments

    def ingest(self, date):
        self.df = self.comments.dataFrame(self.context, date)
        return self

    def write(self, date):
        self.df.write.option("header", "true").csv('data/%s/%s' % (self.name, date))

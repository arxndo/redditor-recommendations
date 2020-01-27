from Calendar import Calendar
from Mergeable import Mergeable

class GraphObject(Sequentiable, Mergeable):

    def init__(self, context, comments):
        self.context = context
        self.comments = comments

    def write(self, date):
        self.df.write.option("header", "true").csv(self.name)

import sys
sys.path.insert(0, 'src/classes/abstract')
sys.path.insert(0, 'src/classes/concrete')
sys.path.insert(0, 'src/classes')
from Comments import Comments
from Calendar import Calendar
from MyContext import MyContext
from Edges import Edges

comments = Comments( comment_url = "https://files.pushshift.io/reddit/comments", \
                           comment_path = 'files.pushshift.io/reddit/comments', \
                           s3BucketName = "romeosredditcomments" )

context = MyContext().context()

startDate = '2005-12'
endDate = '2006-02'

edges = Edges(context, comments)
#edges.process(startDate, endDate)
edges.merge(startDate, endDate)


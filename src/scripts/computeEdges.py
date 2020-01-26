import sys
sys.path.insert(0, 'src/classes')
from Comments import Comments
from MyContext import MyContext
from Scores import Scores
from Utility import Utility as ut

comments = Comments( comment_url = "https://files.pushshift.io/reddit/comments", \
                           comment_path = 'files.pushshift.io/reddit/comments', \
                           s3BucketName = "romeosredditcomments" )

context = MyContext().context()

edges = Edges(context, comments)

edges = ut.process( edges, '2005-12', '2006-02')

edges = ut.merge( edges )

ut.write( edges )

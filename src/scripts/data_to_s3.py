import sys
sys.path.insert(0, 'src/classes')
sys.path.insert(0, 'src/classes/abstract')
sys.path.insert(0, 'src/classes/concrete')
sys.path.insert(0, 'src/classes')
from Comments import Comments
from Calendar import Calendar

comments = Comments( comment_url = "https://files.pushshift.io/reddit/comments", \
                           comment_path = 'files.pushshift.io/reddit/comments', \
                           s3BucketName = "romeosredditcomments" )


startDate = '2006-03'
endDate = '2006-05'

comments.process(startDate, endDate)

#comments.show(12, 2005)

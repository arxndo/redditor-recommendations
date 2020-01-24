import sys
sys.path.insert(0, 'src/classes')
from Comments import Comments
from Calendar import Calendar
from MyContext import MyContext
from AuthorScores import AuthorScores

comments = Comments( comment_url = "https://files.pushshift.io/reddit/comments", \
                           comment_path = 'files.pushshift.io/reddit/comments', \
                           s3BucketName = "romeosredditcomments" )


calendar = Calendar( startMonth = 12, \
                            startYear = 2005, \
                            endMonth = 2, \
                            endYear = 2006 )

context = MyContext().context()

AuthorScores().loadComments(context, comments, calendar) \
              .addScores() \
              .write()






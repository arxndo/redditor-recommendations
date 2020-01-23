import sys
sys.path.insert(0, 'src/classes')
from RedditComments import RedditComments
from Calendar import Calendar

comments = RedditComments( comment_url = "https://files.pushshift.io/reddit/comments", \
                           comment_path = 'files.pushshift.io/reddit/comments', \
                           s3BucketName = "romeosbucket" )


calendar = Calendar( startMonth = 5, \
                            startYear = 2005, \
                            endMonth = 2, \
                            endYear = 2006 )

comments.downloadAll( calendar )

comments.show(12, 2005)

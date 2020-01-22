import sys
sys.path.insert(0, 'src/RedditComments')
from RedditComments import RedditComments

comments = RedditComments( comment_url = "https://files.pushshift.io/reddit/comments", \
                           s3BucketName = "romeosbucket" )


comments.downloadBatches( startMonth = 12, \
                            startYear = 2005, \
                            endMonth = 1, \
                            endYear = 2006 )

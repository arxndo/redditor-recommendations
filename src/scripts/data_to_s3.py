import sys
sys.path.insert(0, 'src/classes')
#import RedditComments
from RedditComments import RedditComments

comments = RedditComments( comment_url = "https://files.pushshift.io/reddit/comments", \
                           s3BucketName = "romeosbucket" )


comments.downloadBatches( startMonth = 5, \
                            startYear = 2005, \
                            endMonth = 2, \
                            endYear = 2006 )

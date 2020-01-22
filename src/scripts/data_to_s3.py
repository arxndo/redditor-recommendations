import sys
sys.path.insert(0, 'src/RedditComments')
from RedditComments import RedditComments

comments = RedditComments( comment_url = "https://files.pushshift.io/reddit/comments", \
                           s3BucketName = "romeosbucket" )


comments.downloadBatches( startMonth = 5, \
                            startYear = 2016, \
                            endMonth = 12, \
                            endYear = 2019 )

import sys
sys.path.insert(0, 'src/classes')
from RedditComments import RedditComments
from Calendar import Calendar
from SparkSuite import SparkSuite

comments = RedditComments( comment_url = "https://files.pushshift.io/reddit/comments", \
                           comment_path = 'files.pushshift.io/reddit/comments', \
                           s3BucketName = "romeosredditcomments" )


calendar = Calendar( startMonth = 12, \
                            startYear = 2005, \
                            endMonth = 2, \
                            endYear = 2006 )


sparkSuite = SparkSuite("myApp")
spark = sparkSuite.spark()

month = 12;
year = 2005;
comments.clean(spark, month, year)



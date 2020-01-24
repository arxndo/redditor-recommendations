import sys
sys.path.insert(0, 'src/classes')
from RedditComments import RedditComments
from Calendar import Calendar
from MySpark import MySpark

comments = RedditComments( comment_url = "https://files.pushshift.io/reddit/comments", \
                           comment_path = 'files.pushshift.io/reddit/comments', \
                           s3BucketName = "romeosredditcomments" )


calendar = Calendar( startMonth = 12, \
                            startYear = 2005, \
                            endMonth = 2, \
                            endYear = 2006 )

spark = MySpark().spark()

print("%d authors posted %d comments between %d/%d and %d/%d" \
        % ( comments.countAllAuthors(spark, calendar), \
            comments.countAll(spark, calendar), \
            calendar.startMonth, \
            calendar.startYear, \
            calendar.endMonth, \
            calendar.endYear ) )




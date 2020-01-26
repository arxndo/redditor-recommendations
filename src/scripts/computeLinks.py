import sys
sys.path.insert(0, 'src/classes')
from Comments import Comments
from Calendar import Calendar
from MyContext import MyContext
from Links import Links

comments = Comments( comment_url = "https://files.pushshift.io/reddit/comments", \
                           comment_path = 'files.pushshift.io/reddit/comments', \
                           s3BucketName = "romeosredditcomments" )

context = MyContext().context()

Links(context, comments).process('2005-12', '2006-02').merge()

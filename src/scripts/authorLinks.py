import sys
sys.path.insert(0, 'src/classes')
from Comments import Comments
from Calendar import Calendar
from MyContext import MyContext
from AuthorLinks import AuthorLinks

comments = Comments( comment_url = "https://files.pushshift.io/reddit/comments", \
                           comment_path = 'files.pushshift.io/reddit/comments', \
                           s3BucketName = "romeosredditcomments" )

context = MyContext().context()

AuthorLinks(context, comments) \
    .process('2005-12', '2006-02')

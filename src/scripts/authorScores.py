import sys
sys.path.insert(0, 'src/classes')
from Comments import Comments
from MyContext import MyContext
from AuthorScores import AuthorScores

comments = Comments( comment_url = "https://files.pushshift.io/reddit/comments", \
                           comment_path = 'files.pushshift.io/reddit/comments', \
                           s3BucketName = "romeosredditcomments" )

context = MyContext().context()

AuthorScores(context, comments) \
    .process('2005-12', '2006-02')






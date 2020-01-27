import sys
sys.path.insert(0, 'src/classes/abstract')
sys.path.insert(0, 'src/classes/concrete')
sys.path.insert(0, 'src/classes')
from Comments import Comments
from MyContext import MyContext
from Scores import Scores

comments = Comments( comment_url = "https://files.pushshift.io/reddit/comments", \
                           comment_path = 'files.pushshift.io/reddit/comments', \
                           s3BucketName = "romeosredditcomments" )

context = MyContext().context()

startDate = '2005-12'
endDate = '2006-02'
scores = Scores(context, comments)

scores.process(startDate, endDate) \
      .merge(startDate, endDate)


import sys
sys.path.insert(0, 'src/classes/abstract')
sys.path.insert(0, 'src/classes/concrete')
sys.path.insert(0, 'src/classes')
from Comments import Comments
from MyContext import MyContext
from Nodes import Nodes
import yaml


with open('config.yml', 'r') as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)


comments = Comments( comment_url = cfg['reddit']['comments_url'], \
                           comment_path = cfg['reddit']['comments_path'], \
                           s3BucketName = cfg['s3']['commentsBucket'] )


context = MyContext().context()

startDate = '2005-12'
endDate = '2006-02'
nodes = Nodes(context, comments)

#nodes.process(startDate, endDate) \
nodes.merge(startDate, endDate)


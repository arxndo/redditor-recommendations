import sys
sys.path.insert(0, 'src/classes/abstract')
sys.path.insert(0, 'src/classes/concrete')
sys.path.insert(0, 'src/classes')
from Comments import Comments
from Calendar import Calendar
from MyContext import MyContext
from Edges import Edges
import yaml


with open('config.yml', 'r') as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)


comments = Comments( cfg['reddit']['commentsUrl'], \
                     cfg['reddit']['commentsPath'], \
                     cfg['s3']['commentsBucket'] )

context = MyContext().context()

edges = Edges(context, comments, cfg['s3']['edgesBucket'])

edges.process(cfg['dates']['startDate'], cfg['dates']['endDate'])

#edges.merge(cfg['dates']['startDate'], cfg['dates']['endDate'])


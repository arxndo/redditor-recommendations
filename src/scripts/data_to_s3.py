import sys
sys.path.insert(0, 'src/classes')
sys.path.insert(0, 'src/classes/abstract')
sys.path.insert(0, 'src/classes/concrete')
sys.path.insert(0, 'src/classes')
from Comments import Comments
from Calendar import Calendar
import yaml

with open('config.yml', 'r') as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)


comments = Comments( cfg['reddit']['commentsUrl'], \
                     cfg['reddit']['commentsPath'], \
                     cfg['s3']['commentsBucket'] )


comments.process(cfg['dates']['startDate'], cfg['dates']['endDate'])


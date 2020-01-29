sys.path.insert(0, 'src/classes/abstract')
sys.path.insert(0, 'src/classes/concrete')
sys.path.insert(0, 'src/classes')
sys.os.environ['PYSPARK_PYTHON'] = '/usr/bin/python3.5'
sys.os.environ["PYSPARKDRIVER_PYTHON"]= "/usr/bin/python3.5"

from Comments import Comments
from Calendar import Calendar
from MyContext import MyContext
from Edges import Edges
from Configuration import Configuration

cfg = Configuration.configuration('config.yml')

comments = Comments(cfg)

context = MyContext().context(cfg)

edges = Edges(context, comments, cfg['s3']['edgesBucket'])

edges.process(cfg['dates']['startDate'], cfg['dates']['endDate'])

#edges.merge(cfg['dates']['startDate'], cfg['dates']['endDate'])


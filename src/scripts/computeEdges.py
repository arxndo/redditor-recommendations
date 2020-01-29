import sys
sys.os.environ['PYSPARK_PYTHON'] = '/usr/bin/python3.5'
sys.os.environ["PYSPARKDRIVER_PYTHON"]= "/usr/bin/python3.5"

from Comments import Comments
from Calendar import Calendar
from MyContext import MyContext
from Edges import Edges
from Configuration import Configuration

cfg = Configuration.configuration('config.yml')

context = MyContext().context(cfg, 'edgeCompute')

edges = Edges(cfg, context)

edges.process(cfg['dates']['startDate'], cfg['dates']['endDate'])

#edges.merge(cfg['dates']['startDate'], cfg['dates']['endDate'])


import sys
sys.os.environ['PYSPARK_PYTHON'] = '/usr/bin/python3.5'
sys.os.environ["PYSPARKDRIVER_PYTHON"]= "/usr/bin/python3.5"

from Comments import Comments
from MyContext import MyContext
from Nodes import Nodes

cfg = Configuration.configuration('config.yml')

comments = Comments(cfg)

context = MyContext().context(cfg, 'nodeCompute')

nodes = Nodes(context, comments, cfg)

nodes.process(cfg['dates']['startDate'], cfg['dates']['endDate'])



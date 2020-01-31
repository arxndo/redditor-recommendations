import os
os.environ['PYSPARK_PYTHON'] = '/usr/bin/python3.5'
os.environ["PYSPARKDRIVER_PYTHON"]= "/usr/bin/python3.5"

from CleanComments import CleanComments
from MyContext import MyContext
from Nodes import Nodes
from Configuration import Configuration

cfg = Configuration.configuration('config.yml')

comments = Comments(cfg)

context = MyContext().context(cfg)

nodes = Nodes(context, comments, cfg)

nodes.merge(cfg['dates']['startDate'], cfg['dates']['endDate'])



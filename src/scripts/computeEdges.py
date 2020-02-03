import os
os.environ['PYSPARK_PYTHON'] = '/usr/bin/python3.5'
os.environ["PYSPARKDRIVER_PYTHON"]= "/usr/bin/python3.5"

from MyContext import MyContext
from Edges import Edges
from Configuration import Configuration

cfg = Configuration.configuration('config.yml')

context = MyContext().context(cfg, 'computeEdges%s_%s' \
                        % (cfg['dates']['startDate'], cfg['dates']['endDate']))

edges = Edges(cfg, context)

edges.process(cfg['dates']['startDate'], cfg['dates']['endDate'])


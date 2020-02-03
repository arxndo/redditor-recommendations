import os
os.environ['PYSPARK_PYTHON'] = '/usr/bin/python3.5'
os.environ["PYSPARKDRIVER_PYTHON"]= "/usr/bin/python3.5"

from MyContext import MyContext
from Configuration import Configuration
from Nodes import Nodes

cfg = Configuration.configuration('config.yml')

context = MyContext().context(cfg, 'computeNodes%s_%s' \
                        % (cfg['dates']['startDate'], cfg['dates']['endDate']))

nodes = Nodes(cfg, context)

nodes.process(cfg['dates']['startDate'], cfg['dates']['endDate'])



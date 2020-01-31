import os
os.environ['PYSPARK_PYTHON'] = '/usr/bin/python3.5'
os.environ["PYSPARKDRIVER_PYTHON"]= "/usr/bin/python3.5"

from MyContext import MyContext
from MergedEdges import MergedEdges
from Configuration import Configuration

cfg = Configuration.configuration('config.yml')

context = MyContext().context(cfg, 'mergeEdges%s_%s' \
                        % (cfg['dates']['startDate'], cfg['dates']['endDate']))

mergedEdges = MergedEdges(context, cfg)

mergedEdges.process(cfg['dates']['startDate'], cfg['dates']['endDate']) \
           .merge(cfg['dates']['startDate'], cfg['dates']['endDate'])

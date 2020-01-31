import os
os.environ['PYSPARK_PYTHON'] = '/usr/bin/python3.5'
os.environ["PYSPARKDRIVER_PYTHON"]= "/usr/bin/python3.5"

from MyContext import MyContext
from MergedEdgeAnalysis import MergedEdgeAnalysis
from Configuration import Configuration

cfg = Configuration.configuration('config.yml')

context = MyContext().context(cfg, 'analysis%s_%s' \
                        % (cfg['dates']['startDate'], cfg['dates']['endDate']))

mergedEdgeAnalysis = MergedEdgeAnalysis(context, cfg)

mergeEdgeAnalysis.process(cfg['dates']['startDate'], cfg['dates']['endDate'])

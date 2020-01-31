import os
os.environ['PYSPARK_PYTHON'] = '/usr/bin/python3.5'
os.environ["PYSPARKDRIVER_PYTHON"]= "/usr/bin/python3.5"

from MyContext import MyContext
from EdgeAnalysis import EdgeAnalysis
from Configuration import Configuration

cfg = Configuration.configuration('config.yml')

context = MyContext().context(cfg, 'analysis%s_%s' \
                        % (cfg['dates']['startDate'], cfg['dates']['endDate']))

edgeAnalysis = EdgeAnalysis(context, cfg)

edgeAnalysis.process(cfg['dates']['startDate'], cfg['dates']['endDate'])

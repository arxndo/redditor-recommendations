import os
os.environ['PYSPARK_PYTHON'] = '/usr/bin/python3.5'
os.environ["PYSPARKDRIVER_PYTHON"]= "/usr/bin/python3.5"

from MyContext import MyContext
from MergedNodes import MergedNodes
from Configuration import Configuration

cfg = Configuration.configuration('config.yml')

context = MyContext().context(cfg, 'mergeNodes%s_%s' \
                        % (cfg['dates']['startDate'], cfg['dates']['endDate']))

mergedNodes = MergedNodes(context, cfg)

mergedNodes.process(cfg['dates']['startDate'], cfg['dates']['endDate'])



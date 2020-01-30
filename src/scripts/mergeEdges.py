import sys
sys.os.environ['PYSPARK_PYTHON'] = '/usr/bin/python3.5'
sys.os.environ["PYSPARKDRIVER_PYTHON"]= "/usr/bin/python3.5"

from CleanComments import CleanComments
from MyContext import MyContext
from MergedEdges import MergedEdges
from Configuration import Configuration

cfg = Configuration.configuration('config.yml')

context = MyContext().context(cfg, 'mergeEdges%s_%s' \
                        % (cfg['dates']['startDate'], cfg['dates']['endDate']))

mergedEdges = MergedEdges(context, cfg)

edges.merge(cfg['dates']['startDate'], cfg['dates']['endDate'])

import sys
sys.os.environ['PYSPARK_PYTHON'] = '/usr/bin/python3.5'
sys.os.environ["PYSPARKDRIVER_PYTHON"]= "/usr/bin/python3.5"

from CleanComments import CleanComments
from Configuration import Configuration
from MyContext import MyContext

cfg = Configuration.configuration('config.yml')

context = MyContext().context(cfg, 'cleanData')

cleanComments = CleanComments(context, cfg)

cleanComments.process(cfg['dates']['startDate'], cfg['dates']['endDate'])


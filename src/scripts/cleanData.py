import os
os.environ['PYSPARK_PYTHON'] = '/usr/bin/python3.5'
os.environ["PYSPARKDRIVER_PYTHON"]= "/usr/bin/python3.5"

from Configuration import Configuration
from MyContext import MyContext
from CleanComments import CleanComments

cfg = Configuration.configuration('config.yml')

context = MyContext().context(cfg, 'cleanData')

cleanComments = CleanComments(cfg, context)

cleanComments.process(cfg['dates']['startDate'], cfg['dates']['endDate'])


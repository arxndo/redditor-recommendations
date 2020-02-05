import os
os.environ['PYSPARK_PYTHON'] = '/usr/bin/python3.5'
os.environ["PYSPARKDRIVER_PYTHON"]= "/usr/bin/python3.5"

from Configuration import Configuration
from MyContext import MyContext
from DailyComments import DailyComments

cfg = Configuration.configuration('config.yml')

context = MyContext().context(cfg, 'dailyComments%s_%s' \
                        % (cfg['dates']['startDate'], cfg['dates']['endDate']))

dailyComments = DailyComments(cfg, context)

dailyComments.process(cfg['dates']['startDate'], cfg['dates']['endDate'])


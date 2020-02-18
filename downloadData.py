#import sys
#sys.path.insert(0, '~/redditor-recommendations/spark/classes/download')
#__pacage__ = None
from spark.classes.download.RawComments import RawComments
#from RawComments import RawComments
from utils.classes.Configuration import Configuration

cfg = Configuration.configuration('config.yml')

rawComments = RawComments(cfg)

rawComments.process(cfg['dates']['startDate'], cfg['dates']['endDate'])


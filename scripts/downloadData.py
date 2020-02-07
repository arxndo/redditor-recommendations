from RawComments import RawComments
from Configuration import Configuration

cfg = Configuration.configuration('config.yml')

rawComments = RawComments(cfg)

rawComments.process(cfg['dates']['startDate'], cfg['dates']['endDate'])


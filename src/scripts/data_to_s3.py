from Comments import Comments
from Configuration import Configuration

cfg = Configuration.configuration('config.yml')

comments = Comments(cfg)

comments.process(cfg['dates']['startDate'], cfg['dates']['endDate'])


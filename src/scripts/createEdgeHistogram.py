from Configuration import Configuration
from EdgeHistogram import EdgeHistogram
from MyContext import MyContext

cfg = Configuration.configuration('config.yml')

context = MyContext().context(cfg, 'edgeHistogram%s_%s' \
                        % (cfg['dates']['startDate'], cfg['dates']['endDate']))

edgeHistogram = EdgeHistogram(context, cfg)

edgeHistogram.process(cfg['dates']['startDate'], cfg['dates']['endDate'])

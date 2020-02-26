import os
from Configuration import Configuration
from Importer import Importer

os.environ['PYSPARK_PYTHON'] = '/usr/bin/python3.5'
os.environ["PYSPARKDRIVER_PYTHON"]= "/usr/bin/python3.5"
cfg = Configuration.configuration('config.yml')
importer = Importer(cfg)
importer.process(cfg['dates']['startDate'], cfg['dates']['endDate'])

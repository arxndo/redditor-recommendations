from Configuration import Configuration
from NeoReddit import NeoReddit 

cfg = Configuration.configuration('config.yml')
nr = NeoReddit(cfg)
print(nr.topSub('arxndo'))

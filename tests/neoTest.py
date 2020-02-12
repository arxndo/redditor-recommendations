from Configuration import Configuration
from NeoReddit import NeoReddit 

cfg = Configuration.configuration('config.yml')
nr = NeoReddit(cfg)

print('')
result = nr.authorToSubs('arxndo', 3)
for item in result.records():
    print(item['subreddit'])

print('')
result = nr.subToAuthors('batman', 3)
for item in result.records():
    print(item['author'])



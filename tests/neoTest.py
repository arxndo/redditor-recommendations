from Configuration import Configuration
from NeoReddit import NeoReddit 

cfg = Configuration.configuration('config.yml')
nr = NeoReddit(cfg)

authorName = 'arxndo'
print('\nSubs subscribed to by: %s' % authorName)
result = nr.authorToSubs(authorName, 3)
for item in result:
    print('sub: %s, score: %d' %(item[0], item[1]))

subName = 'Patriots'
print('\nRedditors subscribed to: %s' % subName)
result = nr.subToAuthors(subName, 10)
for item in result:
    name = item[0]
    score = item[1]
    print('\n%s\nscore: %d' %(name, score))
    similarity = nr.cosineSimilarity(authorName, name)
    print('similarity: %f' % similarity)
    subList = nr.authorToSubs(name,10)
    for subItem in subList:
        print(subItem[0])



name1 = 'arxndo'
name2 = 'GovSchwarzenegger'
result = nr.cosineSimilarity(name1, name2)
print('\n%s,%s: %f' % (name1, name2, result))

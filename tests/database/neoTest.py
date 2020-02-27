from src.utils.Configuration import Configuration
from src.database.classes.NeoReddit import NeoReddit 
import timeit

cfg = Configuration.configuration('config.yml')
nr = NeoReddit(cfg)

print('Warming up cache\n')
tic = timeit.default_timer()
nr.warmUpCache()
toc = timeit.default_timer()
print('\n%.4f seconds\n' % (toc - tic))

exit()

tic = timeit.default_timer()
authors = nr.authorToAuthors('arxndo', 5)
for item in authors:
    print(item)
toc = timeit.default_timer()
print('%.4f seconds\n' % (toc - tic))

tic = timeit.default_timer()
authors = nr.authorToAuthors('arxndo', 5)
for item in authors:
    print(item)
toc = timeit.default_timer()
print('%.4f seconds\n' % (toc - tic))

authors = ['williamshatner', 'GovSchwarzenegger', 'kn0thing']
    
item1 = nr.authorToSubs(authors[0], 3)
subName1 = []
for sub in item1:
    subName1.append(sub[0])

item2 = nr.authorToSubs(authors[1], 3)
subName2 = []
for sub in item2:
    subName2.append(sub[0])

item3 = nr.authorToSubs(authors[2], 3)
subName3 = []
for sub in item3:
    subName3.append(sub[0])

subName = 'Patriots'
authors = nr.subToAuthors(subName, 3)
for authorInfo in authors:
    print(authorInfo[0])

print(subName1[0])
print(subName1[1])
print(subName1[2])
print(subName2[0])
print(subName2[1])
print(subName2[2])
print(subName3[0])
print(subName3[1])
print(subName3[2])

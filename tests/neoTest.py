from Configuration import Configuration
from NeoReddit import NeoReddit 

cfg = Configuration.configuration('config.yml')
nr = NeoReddit(cfg)


authorName = 'arxndo'

authors = nr.authorToAuthors(authorName, 3)
for item in authors:
    print(item)

    
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


print(subName1[0])
print(subName1[1])
print(subName1[2])
print(subName2[0])
print(subName2[1])
print(subName2[2])
print(subName3[0])
print(subName3[1])
print(subName3[2])

from pandas import pandas as pd

fileName = 'full-author-sub'
df = pd.read_csv('tmp/%s.csv' % fileName, header=None)

df.columns = ['author', 'sub', 'score']

df = df.sort_values(by='score', ascending=False)

df.to_csv(r'tmp/sorted-author-sub.csv', index=None, header=True)


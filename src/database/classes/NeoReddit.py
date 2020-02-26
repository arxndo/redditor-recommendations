from neo4j import GraphDatabase
import functools

class NeoReddit:

    def __init__(self, cfg):
        self.driver = GraphDatabase \
                        .driver( cfg['neo4j']['address'], \
                            auth =\
                            (cfg['neo4j']['username'], \
                             cfg['neo4j']['password']))

    def getKarma(self, name):
        with self.driver.session() as session:
            tx = session.begin_transaction()
            result = tx.run("match (a:author {name: {name}}) return a.score as score", name=name)  
        for item in result.records():
            karma = item['score']
        return karma


    @functools.lru_cache(maxsize = None)
    def authorToAuthors(self, name, n):
        subs = self.authorToSubs(name, n)
        authorRecords = []
        for sub in subs:
            subName = sub[0]
            authorList = self.subToAuthors(subName, 1)
            authorRecords.append(authorList[0])
        return authorRecords


    @functools.lru_cache(maxsize = None)
    def authorToSubs(self, name, n):
        with self.driver.session() as session:
            tx = session.begin_transaction()
            result = tx.run("match (a:author {name: {name}})-[r:post_to]->(s:subreddit) with s.name as sname, r.score as rscore order by rscore desc with collect([sname,rscore])[..{n}] as topsubs unwind topsubs as q return q[0] as subreddit, q[1] as score", name=name, n=n)  
        subList = []
        for item in result.records():
            subList.append((item['subreddit'], item['score']))
        return subList

    @functools.lru_cache(maxsize = None)
    def subToAuthors(self, name, n):
        with self.driver.session() as session:
            tx = session.begin_transaction()
            result = tx.run("match (a:author)-[r:post_to]->(s:subreddit {name: {name}}) with a.name as aname, r.score as rscore order by rscore desc with collect([aname,rscore])[..{n}] as topusers unwind topusers as q return q[0] as author, q[1] as score", name=name,n=n)
        authorList = []
        for item in result.records():
            authorList.append((item['author'], item['score']))
        return authorList


    def cosineSimilarity(self, name1, name2):
        with self.driver.session() as session:
            tx = session.begin_transaction()
            result = tx.run("MATCH (p1:author {name: {name1}})-[likes1:post_to]->(cuisine) MATCH (p2:author {name: {name2}})-[likes2:post_to]->(cuisine) RETURN p1.name AS from, p2.name AS to, algo.similarity.cosine(collect(likes1.score), collect(likes2.score)) AS similarity", name1=name1,name2=name2)
        for item in result.records():
            return round(item['similarity'] , 2)

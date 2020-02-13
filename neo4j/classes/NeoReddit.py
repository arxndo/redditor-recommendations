from neo4j import GraphDatabase

class NeoReddit:

    def __init__(self, cfg):
        self.driver = GraphDatabase \
                        .driver( cfg['neo4j']['address'], \
                            auth =\
                            (cfg['neo4j']['username'], \
                             cfg['neo4j']['password']))

    def authorToAuthors(self, name, n):
        subs = self.authorToSubs(name, n)
        authors = []
        for sub in subs:
            subName = sub[0]
            author = self.subToAuthors(subName, 1)
            authorName = author[0]
            authors.append(authorName)
        if len(authors) == 1:
            return authors[0]
        else:
            return authors

    def topSub(self, name):
        with self.driver.session() as session:
            tx = session.begin_transaction()
            topSub = ''
            topScore = 0
            for record in tx.run("MATCH (a:author{name: {name}})"
                                "-[:post_to]->(s:subreddit) " \
                                "RETURN s.name, s.score", \
                                 name = name):
                if (record['s.score'] > topScore):
                    topScore = record['s.score']
                    topSub = record['s.name']
            return topSub

    def authorToSubs(self, name, n):
        with self.driver.session() as session:
            tx = session.begin_transaction()
            result = tx.run("match (:author {name: {name}})-[r:post_to]->(s:subreddit) with s.name as sname, r.score as rscore order by rscore desc with collect([sname,rscore])[..{n}] as topsubs unwind topsubs as q return q[0] as subreddit, q[1] as score", name=name, n=n)  
        subList = []
        for item in result.records():
            subList.append((item['subreddit'], item['score']))
        if len(subList) == 1:
            return subList[0]
        else:
            return subList


    def subToAuthors(self, name, n):
        with self.driver.session() as session:
            tx = session.begin_transaction()
            result = tx.run("match (a:author)-[r:post_to]->(s:subreddit {name: {name}}) with a.name as aname, r.score as rscore order by rscore desc with collect([aname,rscore])[..{n}] as topusers unwind topusers as q return q[0] as author, q[1] as score", name=name,n=n)
        authorList = []
        for item in result.records():
            authorList.append((item['author'], item['score']))
        if len(authorList) == 1:
            return authorList[0]
        else:
            return authorList


    def cosineSimilarity(self, name1, name2):
        with self.driver.session() as session:
            tx = session.begin_transaction()
            result = tx.run("MATCH (p1:author {name: {name1}})-[likes1:post_to]->(cuisine) MATCH (p2:author {name: {name2}})-[likes2:post_to]->(cuisine) RETURN p1.name AS from, p2.name AS to, algo.similarity.cosine(collect(likes1.score), collect(likes2.score)) AS similarity", name1=name1,name2=name2)
        for item in result.records():
            return round(item['similarity'] , 2)

from neo4j import GraphDatabase

class NeoReddit:

    def __init__(self, cfg):
        self.driver = GraphDatabase \
                        .driver( cfg['neo4j']['address'], \
                            auth =\
                            (cfg['neo4j']['username'], \
                             cfg['neo4j']['password']))


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
            return result

    def subToAuthors(self, name, n):
        with self.driver.session() as session:
            tx = session.begin_transaction()
            result = tx.run("match (a:author)-[r:post_to]->(s:subreddit {name: {name}}) with a.name as aname, r.score as rscore order by rscore desc with collect([aname,rscore])[..{n}] as topusers unwind topusers as q return q[0] as author, q[1] as score", name=name,n=n)
            return result

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

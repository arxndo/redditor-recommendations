from neo4j import GraphDatabase

driver = GraphDatabase.driver('bolt://127.0.0.1:7687', auth=('neo4j', 'insight'))

def print_friends_of(tx, name):
    numberOfSubs = 0
    topSub = ''
    topScore = 0
    for record in tx.run("MATCH (a:author{name: {name}})-[:post_to]->(s:subreddit) " \
                         "RETURN s.name, s.score", name = name):
        if (record['s.score'] > topScore):
            topScore = record['s.score']
            topSub = record['s.name']
        numberOfSubs += 1

    print('')
    print('User input: %s' % name)
    print('%d subreddits.' % numberOfSubs)
    print('Larged subreddt: %s' \
            % topSub)
    print('')

with driver.session() as session:
    #session.read_transaction(print_friends_of, "Beararms")
    #session.read_transaction(print_friends_of, "Holzmann")
    session.read_transaction(print_friends_of, "arxndo")


from neo4j import GraphDatabase

driver = GraphDatabase.driver('bolt://127.0.0.1:7687', auth=('neo4j', '8xvel3pq'))

def print_friends_of(tx, name):
    numberOfFriends = 0
    best_author = ''
    top_karma = 0
    for record in tx.run("MATCH (a:author)-[:edge]-(f) "
                         "WHERE a.name = {name} "
                         "RETURN f.name, f.karma", name=name):
        if (record['f.karma'] > top_karma):
            top_kamra = record['f.karma']
            best_author = record['f.name']
        numberOfFriends += 1

    print('')
    print('User input: %s' % name)
    print('%d similar redditors.' % numberOfFriends)
    print('Highest karma redditor in immediate network: %s' \
            % best_author)
    print('')

with driver.session() as session:
    #session.read_transaction(print_friends_of, "Beararms")
    #session.read_transaction(print_friends_of, "Holzmann")
    session.read_transaction(print_friends_of, "wootfish")


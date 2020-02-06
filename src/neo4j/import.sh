sudo /usr/bin/neo4j-admin import \
       	--nodes:author="/var/lib/neo4j/import/authors_header.csv,/var/lib/neo4j/import/authors.csv" \
	--relationships:edge="/var/lib/neo4j/import/edges_header.csv,/var/lib/neo4j/import/edges.csv"



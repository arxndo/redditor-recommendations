sudo /usr/bin/neo4j-admin import \
       	--nodes:author= \
		"~/redditor-recommendations/headers/authors_header.csv,~/redditor-recommendations/tmp/authors.csv" \
       	--nodes:subreddit= \
		"~/redditor-recommendations/headers/subs_header.csv,~/redditor-recommendations/tmp/subs.csv" \
	--relationships:edge= \
		"~/redditor-recommendations/headers/edges_header.csv,/var/lib/neo4j/import/edges.csv" \
	--ignore-missing-nodes true



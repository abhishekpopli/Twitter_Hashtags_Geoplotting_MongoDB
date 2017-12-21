from pprint import pprint
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017')
db = client.twitterdb

cursor = db.twitter_search.find().limit(1)
for result_object in cursor:
    pprint(result_object)
#db.twitter_search.remove({})


#Network graph

# import networkx as nx
# G = nx.Graph()
# G.add_edge(23, 89, weight=34.9)
# G.add_edge(75, 14, weight=28.5)
#
# import networkx as nx
# G=nx.Graph()
# G.add_edges_from([(1,2),(1,3),(1,4),(3,4)])
# G.nodes(data=True)
# G.node[1]['attribute']='value'
# G.nodes(data=True)
# nx.write_graphml(G,'so.graphml')



import os
from elasticsearch import Elasticsearch

index = 'library'
type = 'newspaper'
port = 9200
host = os.environ['ES_HOST'] or 'localhost'
es = Elasticsearch([{'host': host, 'port': port}])


def connect_elasticsearch():
    is_connected = False
    while not is_connected:
        print('Connecting to Elasticsearch')
        try:
            health = es.cluster.health()
            print(health)
            is_connected = True
        except Exception as err:
            print('Connection failed, Retrying...', err)

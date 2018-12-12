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


#TODO: Implement a 'mapping' for the newspaper data schema
def put_newspaper_mapping():
    pass


# Helper function to reset the Elasticsearch index
def reset_index():
    if es.indices.exists({index}):
        es.indices.delete({index})

    es.indices.create({index})
    put_newspaper_mapping()
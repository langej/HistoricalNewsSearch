import os
import pprint
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
            pprint.pprint(health)
            is_connected = True
        except Exception as err:
            print('Connection failed, Retrying...', err)


def create_index(elasticsearch_object, index_name='library'):
    created = False
    settings = {
        'settings': {
            'number_of_shards': 1,
            'number_of_replicas': 0
        },
        'mappings': {
            'members': {
                'dynamic': 'strict',
                'properties': {
                    'date': {'type': 'date'},
                    'newspaper_number': {'type': 'integer'},
                    'page_number': {'type': 'integer'},
                    'edition': {'type': 'integer'},
                    'issue': {'type': 'integer'},
                    'text': {'type': 'text'}
                }
            }
        }
    }

    try:
        if not elasticsearch_object.indices.exists(index_name):
            # Ignore 400 means to ignore 'Index already exist' error
            elasticsearch_object.indices.create(index=index_name, ignore=400, body=settings)
            print('Created Index')
            created = True
    except Exception as ex:
        print(str(ex))
    finally:
        return created


# Helper function to reset the Elasticsearch index
def reset_index():
    if es.indices.exists({index}):
        es.indices.delete({index})

    create_index(es, index)

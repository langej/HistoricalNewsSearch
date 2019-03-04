import os
import pprint
import json
from elasticsearch import Elasticsearch, helpers
import logger
import time


class ElasticsearchHelper(object):

    def __init__(self):
        self.Index = 'library'
        self.Type = 'newspaper'
        self.Port = 9200
        self.Host = os.environ['ES_HOST'] or 'localhost'
        self.Es = Elasticsearch([{'host': self.Host, 'port': self.Port}])
        self.connect_elasticsearch()

    def connect_elasticsearch(self):
        is_connected = False
        while not is_connected:
            print('Connecting to Elasticsearch')
            try:
                health = self.Es.cluster.health()
                pprint.pprint(health)
                is_connected = True
            except Exception as err:
                print('Connection failed, Retrying...', err)
                time.sleep(5)
                
        self.reset_index()
        self.import_Data()

    def create_index(self):
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
                        'Year': {'type': 'text'},
                        'Month': {'type': 'text'},
                        'Day': {'type': 'text'},
                        'NewspaperNumber': {'type': 'text'},
                        'PageNumber': {'type': 'text'},
                        'Edition': {'type': 'text'},
                        'Issue': {'type': 'text'},
                        'Text': {'type': 'text'}
                    }
                }
            }
        }

        try:
            print(self.Es.indices.exists(self.Index))
            if not self.Es.indices.exists(self.Index):
                # Ignore 400 means to ignore 'Index already exist' error
                self.Es.indices.create(index=self.Index, ignore=400, body=settings)
                print('Created Index')
                created = True
        except Exception as ex:
            print(str(ex))
        finally:
            return created

    def import_Data(self):
        helpers.bulk(self.Es, self.import_helper('./Xml_Converter/Data/Text/'), index=self.Index, doc_type=self.Type)

    def import_helper(self, directory):
        for filename in os.listdir(directory):
            with open(directory + filename, 'r') as open_file:
                yield json.load(open_file)

    def search(self, input, size):
        if input == 'all':
            res = helpers.scan(self.Es, query={"query": {"match_all": {}}}, index=self.Index,
                               doc_type=self.Type)
        else:
            res = helpers.scan(self.Es, query=self.get_query(input),
                               index=self.Index, doc_type=self.Type)
        result = dict()
        result_ids = []
        for item in res:
            if len(result) == size:
                break
            result[item.get('_id')] = item
            result_ids.append(item.get('_id'))
        if len(result) == 0:
            return {"Items": 0}
        else:
            logger.write_log(input, result_ids[0:10])
            return result

    def get_query(self, input):
        return {
            "query": {
                "bool": {
                    "should": [
                        {"match": {"Year": input}},
                        {"match": {"Month": input}},
                        {"match": {"Day": input}},
                        {"match": {"NewspaperNumber": input}},
                        {"match": {"PageNumber": input}},
                        {"match": {"Edition": input}},
                        {"match": {"Issue": input}},
                        {"match": {"Text": input}}
                    ]
                }
            }
        }

    # Helper function to reset the Elasticsearch index
    def reset_index(self):
        if self.Es.indices.exists(self.Index):
            self.Es.indices.delete(self.Index)
        #self.create_index()


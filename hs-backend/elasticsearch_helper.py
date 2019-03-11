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
                time.sleep(10)

        self.reset_index()
        self.import_Data()

    def create_index(self):
        settings = {
            "settings": {
                "analysis": {
                    "filter": {
                        "my_stop": {
                            "type": "stop",
                            "stopwords": "_german_"
                        }
                    }
                }
            }
        }
        # Ignore 400 means to ignore 'Index already exist' error
        self.Es.indices.create(index=self.Index, ignore=400, body=settings)

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
        dic = self.split_input(input)
        return {
            "query": {
                "bool": {
                    "should": [
                        {"match": {"Year": dic['Year']}},
                        {"match": {"Month": dic['Month']}},
                        {"match": {"Day": dic['Day']}},
                        {"match": {"NewspaperNumber": dic['NewspaperNumber']}},
                        {"match": {"PageNumber": dic['PageNumber']}},
                        {"match": {"Edition": dic['Edition']}},
                        {"match": {"Issue": dic['Issue']}},
                        {"match": {"Text": dic['Text']}}
                    ]
                }
            }
        }

    def split_input(self, input):
        query = {'Year': input, 'Month': input, 'Day': input, 'NewspaperNumber': input, 'PageNumber': input,
                 'Edition': input, 'Issue': input, 'Text': input}
        input_split = input.split(' ')
        for wort in input_split:
            if 'year:' in wort:
                year = input.split('Year:')
                query['Year'] = year[-1]
            elif 'month:' in wort:
                month = input.split('Month:')
                query['Month'] = month[-1]
            elif 'day:' in wort:
                day = input.split('Day:')
                query['Day'] = day[-1]
            elif 'newspapernumber:' in wort:
                newspaper_number = input.split('NewspaperNumber:')
                query['NewspaperNumber'] = newspaper_number[-1]
            elif 'pagenumber:' in wort:
                page_number = input.split('PageNumber:')
                query['PageNumber'] = page_number[-1]
            elif 'edition:' in wort:
                edition = input.split('Edition:')
                query['Edition'] = edition[-1]
            elif 'issue:' in wort:
                issue = input.split('Issue:')
                query['Issue'] = issue[-1]
            elif 'text:' in wort:
                text = input.split('Text:')
                query['Text'] = text[-1]
        print(query)
        return query

    # Helper function to reset the Elasticsearch index
    def reset_index(self):
        if self.Es.indices.exists(self.Index):
            self.Es.indices.delete(self.Index)
            self.create_index()



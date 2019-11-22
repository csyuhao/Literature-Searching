import json
import configure
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk


class Storage(object):
    def __init__(self):
        elastic_node = configure.ELASTICSEARCH_NODE
        self.index_name = elastic_node['index_name']
        self.index_type = elastic_node['index_type']
        self.es = Elasticsearch(elastic_node['ip'], port=elastic_node['port'], http_auth=(elastic_node['name'], elastic_node['passwd']))

    def bulk_Index_Data(self, data):
        '''
        params:
            data    books
        return:
            success    True, insert success
        '''
        ACTIONS = []
        for i, book in enumerate(data):
            action = {
                "_index": self.index_name,
                "_type": self.index_type,
                "_id": i + 1,
                "_source": book
            }
            ACTIONS.append(action)
            # batch process
        success, _ = bulk(self.es,
                          ACTIONS,
                          index=self.index_name,
                          raise_on_error=True)
        return success == 200

    def search(self, body):
        resp = self.es.search(index=self.index_name, body=body)
        with open('log.json', 'w+') as f:
            json.dump(resp, f)


# just for test
if __name__ == "__main__":
    from crawler import Crawler
    crawler = Crawler(query='all:electron', max_entries=200)
    books = crawler.requests()
    storage = Storage()
    success = storage.bulk_Index_Data(books)
    print(success)

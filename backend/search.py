from storage import Storage
from elasticsearch import Elasticsearch


class Search(object):
    def __init__(self):
        self.storage = Storage()

    def search(self):
        # query = {
        #     'query': {
        #         'match': {
        #             'summary': {
        #                 'query': 'Electrons',
        #                 'operator': 'and',
        #                 'fuzziness': 'AUTO'
        #             }
        #         }
        #     }
        # }
        query = {
            'query': {
                'match': {
                    'authors.name': {
                        'query': 'Bai-Jun Zhang',
                        'operator': 'and'
                    }
                }
            }
        }
        self.storage.search(query)


# just for test
if __name__ == "__main__":
    search = Search()
    search.search()

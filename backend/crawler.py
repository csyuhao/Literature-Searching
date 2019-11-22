import json
import configure
import requests
import xml.etree.ElementTree as ET


class Crawler(object):
    def __init__(self, query, max_entries):
        self.API = configure.QUERY_API
        self.params = {
            'search_query': query,
            'start': 0,
            'max_results': max_entries
        }
        self.headers = {
            'user-agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
        }

    def requests(self):
        resp = requests.get(self.API, params=self.params, headers=self.headers)
        books = self.parser_xml(resp.text)
        return books

    def parser_xml(self, data):
        root = ET.fromstring(data)
        books = []
        for entry in root:
            book = dict()
            authors = []
            for attribute in entry:
                _, key = attribute.tag.split('}')
                value = attribute.text
                if key == 'author':
                    author = dict()
                    for attri in attribute:
                        _, key = attri.tag.split('}')
                        value = attri.text
                        author[key] = value
                    authors.append(author)
                book[key] = value
            if len(book) != 0:
                book['authors'] = authors
                books.append(book)
        return books


# just for test
if __name__ == "__main__":
    crawler = Crawler(query='all:electron', max_entries=200)
    books = crawler.requests()
    with open('books_demo.json', 'w+') as f:
        json.dump(books, f)

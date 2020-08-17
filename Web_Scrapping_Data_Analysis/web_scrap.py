import requests
from urllib import request
from bs4 import BeautifulSoup

class web_analysis():

    __url = ''
    __data = ''
    __vlog = None
    __soup = None
    def __init__(self, url):
        self.__url = url

    def retrive_webpage(self):
        try:
            response = request.Request(self.__url)
            html = request.urlopen(response)
        except Exception as e:
            print(e)
        else:
            self.__data = html.read()
            if len(self.__data)>0:
                print('Retrieved succesfully')

    def read_with_bs4(self):
        bs = BeautifulSoup(self.__data, 'html.parser')
        return bs
if __name__ == '__main__':

    autor_names = []
    Page=1
    while(Page!=0 and Page <= 100):
        try:
            response: web_analysis = web_analysis('http://quotes.toscrape.com/page/{}/'.format(Page))
            response.retrive_webpage()
            bs4_obj = response.read_with_bs4()
            header_html = {'class': 'author'}
            autor_container = list(bs4_obj.findAll('small',header_html))
            Page += 1
            print(Page)
            for autor in range(len(autor_container)):
                autor_names.append(autor_container[autor].getText())
        except Exception:
            Page = 0
        finally:
            print(len(autor_names))

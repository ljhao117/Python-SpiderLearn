import requests
import urllib.request
import random
import bs4
from bs4 import BeautifulSoup

def getHtml(url):
    html = urllib.request.urlopen(url).read()
    return html


def getURL(url):
    response = requests.get(url=url, headers={
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) '
                         'AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/83.0.4103.97 Safari/537.36',
           'Accept': 'text/html,application/xhtml+xml,application/xml;'
                     'q=0.9,image/webp,image/apng,*/*;'
                     'q=0.8,application/signed-exchange;v=b3;q=0.9',
           'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    })
    return response.content.decode('utf-8')


def saveHtml(fileName, fileContent):
    with open(fileName.replace('/', '-') + ".html", "w", encoding='utf-8') as file:
        file.write(fileContent)


if __name__ == '__main__':
    # fileContent = getURL('https://cc.163.com/361433/')
    fileContent = getURL(
        'https://www.eejournal.com/article/what-the-faq-are-cpus-mpus-mcus-and-gpus/')
    saveHtml('You don\'t know what you don\'t know', fileContent)
    print('program end')

    # htmlDoc = """<html><head><title>The Dormouse's story</title></head>
    #           <body>
    #           <p class="title"><b>The Dormouse's story</b></p>
              
    #           <p class="story">Once upon a time there were three little sisters; and their names were
    #           <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    #           <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    #           <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    #           and they lived at the bottom of a well.</p>
              
    #           <p class="story">...</p>
    #           """

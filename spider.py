import requests
import urllib.request


def getHtml(url):
    html = urllib.request.urlopen(url).read()
    return html


def saveHtml(file_name, file_content):
    with open(file_name.replace('/', '-') + ".html", "w") as file:
        file.write(file_content)


url = "https://docs.python-requests.org/zh_CN/latest/user/quickstart.html"
html = getHtml(url)
saveHtml("1", "html")
print('end')
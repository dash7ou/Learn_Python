import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

html = urllib.request.urlopen("http://www.dr-chuck.com/page1.html").read()
soup = BeautifulSoup(html, "html.parser")

tags = soup("a")
for tag in tags:
    print(tag.get('href', None))

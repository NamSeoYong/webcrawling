# BeautifulSoup 실행

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page1.html")
#bs = BeautifulSoup(html.read(), 'html.parser')
#bs = BeautifulSoup(html.read(), 'lxml')
bs = BeautifulSoup(html.read(), 'html5lib')
print(bs.h1)
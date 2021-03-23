import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

print("Enter search term")
x=input()
url="https://www.youtube.com/results?search_query=" + x
wbpge=urllib.request.urlopen(url).read()
soup=BeautifulSoup(wbpge, 'html.parser')
print(soup)

#tags=soup('img')
#for tag in tags:
#    print(tag)
-

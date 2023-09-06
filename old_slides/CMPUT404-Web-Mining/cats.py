import urllib
import urllib.request
import time
import json
import bs4

def GET(url):
    req = urllib.request.Request(url)
    req.add_header( "User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0")
    return urllib.request.urlopen(req)

fd = GET("https://imgur.com/r/cats")
content = fd.read()
soup = bs4.BeautifulSoup(content)
#posts = soup.findAll(None,{"class":"post"})
# soup.findAll('a',{"class":"image-list-link"})
print(
    [element.img.attrs["src"] for element in  soup.findAll('a',{"class":"image-list-link"})]
)

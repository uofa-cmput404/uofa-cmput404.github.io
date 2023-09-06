import urllib
import urllib.request
import time
import json
import bs4


def GET(url):
    req = urllib.request.Request(url)
    req.add_header( "User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0")
    content = urllib.request.urlopen(req).read()
    soup = bs4.BeautifulSoup(content)
    return soup

cats = GET("https://imgur.com/r/cats")
res = cats.select('#imagelist img')
 [x["src"].replace("b.","b") for x in res]

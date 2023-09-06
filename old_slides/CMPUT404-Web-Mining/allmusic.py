import urllib
import urllib.request
import time
import json

def GET(url):
    req = urllib.request.Request(url)
    req.add_header( "User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:27.0) Gecko/20100101 Firefox/27.0")
    return urllib.request.urlopen(req)
artist = "devo"
fd = GET("https://www.allmusic.com/search/all/%s" % artist)
content = fd.read()
# now we just have some HTML
# we could use regexes and try to find links
import bs4
soup = bs4.BeautifulSoup(content)
res = soup.findAll(None,{"class":"artist"})
ahref = res[0].findAll(None,{"class":"name"})[0].a
name = ahref.text.strip()
link = ahref.attrs["href"]
related = link + '/related'
rfd = GET(related)
related_content = rfd.read()
soup = bs4.BeautifulSoup(related_content)
res = soup.findAll(None,{"class":"similars"})
ahrefs = [x.a for x in res[0].findAll("li")]
ahrefs = [x.a for x in res[0].findAll("li")]

graph = dict()

def newartist(artist,link):
    return {"url": link, "name": artist, "similar": dict()}

# keep a flat graph
graph[artist] = newartist(artist,link)
links = [(a.text,a.attrs["href"]) for a in ahrefs]
for elm in links:
    (sartist, url) = elm
    if (graph.get(sartist,None) == None):
        graph[sartist] = newartist(sartist,url)
    graph[artist]["similar"][sartist] = url

print(json.dumps(graph,indent=1))

def get_artist(artist):
    uriartist = urllib.parse.urlencode({"":artist})[1:]
    fd = GET("http://www.allmusic.com/search/all/%s" % uriartist)
    content = fd.read()
    soup = bs4.BeautifulSoup(content)
    res = soup.findAll(None,{"class":"artist"})
    ahref = res[0].findAll(None,{"class":"name"})[0].a
    name = ahref.text.strip()
    link = ahref.attrs["href"]
    return newartist(name,link)

def get_similar(artist_entry):
    url = artist_entry["url"]
    related = url + '/related'
    rfd = GET(related)
    related_content = rfd.read()
    soup = bs4.BeautifulSoup(related_content)
    res = soup.findAll(None,{"class":"similars"})
    if len(res) == 0:
        return []
    ahrefs = [x.a for x in res[0].findAll("li")]
    links = [(a.text,a.attrs["href"]) for a in ahrefs]
    return links

def add_similar(graph, artist_entry, links):
    name = artist_entry
    if (name.__class__ != str):
        name = artist_entry["name"]
    for elm in links:
        (sartist, url) = elm
        if (graph.get(sartist,None) == None):
            graph[sartist] = newartist(sartist,url)
        graph[name]["similar"][sartist] = url


for art in graph["devo"]["similar"].keys():
    print("Adding %s" % art)
    if (graph.get(art,None) == None):
        graph[art] = getartist(art)
    links = get_similar( graph[art] )
    print(links)
    add_similar(graph, graph[art], links)



open("devo.json","w").write(json.dumps(graph,indent=1))

# only do the first pass
for art in list(graph.keys()):
    if (len(graph[art]["similar"]) < 1 and 
        not graph[art].get("hit",False)):
            graph[art]["hit"] = True
            print(art)
            links = get_similar( graph[art] )
            add_similar(graph, graph[art], links)
            # save state just in case
            open("ourgraph.json","w").write(json.dumps(graph,indent=1))
            print("...")
            # do you want to get banned from crawling?
            time.sleep(2)

open("end.json","w").write(json.dumps(graph,indent=1))





from functools import reduce
from lxml import etree
import urllib.request
import requests

root = 'https://podcloud.fr'

def getpage(url) :
        print(("url", url))
        u = root + url[0]
        print(("u", u))
        
        txt = urllib.request.urlopen(u).read()
        print(txt)


        u2 = requests.get(u)
        print(u2)
        txt = u2.txt
        return txt



with open("html.html", "r") as fd :    html = fd.read()
#print(html)
dom = etree.HTML(html)
e = dom.xpath("//aaa/div/div")
for ee in e :
        print("=====")
        e1 = ee.xpath("span/a[@data-title]")
        #print(dict(e1[0].items()))
        dd = dict(e1[0].items())
        #print(dd['data-title'])

        print(ee.xpath("span/a[@data-title]/@data-title")[0])
        print(ee.xpath("span/a[@data-title]/@href"))
        print(("href", ee.xpath("a/@href")))
        e3 = ee.xpath("a/@href")
        e2 = ee.xpath("span/div/ul/li[@role='presentation']/a[@target]/@href")
        print(len(e2))
        print(e2)
        if len(e2) == 0 :
                txt = getpage(e3)
                dom1 = etree.HTML(txt)
                aa = dom1.xpath("//*/article/div/div/div/p/a/@href")
                print(("aa", aa))

	#print(dict(e1[0].items())['data-title'])
#print(dict(ee.xpath("span/a")[0].items())['data-title'] for ee in e]
    
if False :
        l = [ dict(ee.xpath("span/a")[0].items())['data-title'] for ee in e]
        print(len(l))
        print(l)
        l = [ee for ee in l if len(ee) > 0]
        print(len(l))
        
        for ee in l :
                #print(ee[0].items())
                title = ee[0].text
                title = reduce(lambda s, p : s.replace(p, '_'), " -()?/[]'`\",:", title) 
                print("youtube-dl https://www.youtube.com/" + dict(ee[0].items())['href'] + " -o %s -x --audio-format mp3 " )
                


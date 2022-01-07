

from functools import reduce
from lxml import etree
with open("html.html", "r") as fd :    html = fd.read()
#print(html)
dom = etree.HTML(html)
e = dom.xpath("//aaa/div/div")
l = [ ee.xpath("div/span/a") for ee in e]
print(len(l))
l = [ee for ee in l if len(ee) > 0]
print(len(l))

for ee in l :
    #print(ee[0].items())
    title = ee[0].text
    title = reduce(lambda s, p : s.replace(p, '_'), " -()?/[]'`\",:", title) 
    print("youtube-dl https://www.youtube.com/" + dict(ee[0].items())['href'] + " -o %s -x --audio-format mp3 " )






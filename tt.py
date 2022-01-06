

from lxml import etree
with open("tt.html", "r") as fd :    html = fd.read()
#print(html)
dom = etree.HTML(html)
e = dom.xpath("//aaa/div/ytd-grid-video-renderer/div/div")
l = [ ee.xpath("div/h3/a") for ee in e]

l = [ee for ee in l if len(ee) > 0]
print(len(l))

for ee in l :
    #print(ee[0].items())
    title = ee[0].text.replace(' ', '_')
    print("youtube-dl https://www.youtube.com/" + dict(ee[0].items())['href'] + " -o %s -x --audio-format mp3 " )








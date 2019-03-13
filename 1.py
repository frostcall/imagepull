#!/usr/bin/env python
import optparse

parser = optparse.OptionParser()
parser.add_option("-s", "--site", dest="site", help="Numerical issue from www.magcloud.com to download images from. MUST have 'Read Sample' enabled.")

(options, arguments) = parser.parse_args()

if not options.site:
    parser.error("Site not given. Re-run with -s #### or -h for help.")

site = options.site
from bs4 import BeautifulSoup
import urllib2
import re
import wget
import os

url = "http://www.magcloud.com/webviewer/"+ site
content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content, features='lxml')
pretty = soup.get_text()

title = soup.title.string.replace("| MagCloud", "")
stitle = title.replace(" ", "")
dpath = "/test/" + site + "-" + stitle

if not os.path.exists(dpath):
    os.mkdir(dpath)
    imgs = re.findall(r'https://s\d.amazonaws.com/storage\d.magcloud.com/image/web/\w*.jpg', pretty)
    urls = ("\n".join(imgs))

    for x in imgs:
        print(x)
        wget.download(x, out=dpath)
        print("")
        print("")
        print("Download for " + title + " COMPLETED.")
        print("[Folder Name: " + dpath + "]")
        print("")

else:
    print("Directory already exsists; not downloading.")

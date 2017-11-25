# http://py4e-data.dr-chuck.net/comments_15162.html Check By this Site
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
ls = list()
# html.parser is the HTML parser included in the standard Python 3 library.
# information on other HTML parsers is here:
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-a-parser
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the Span tags
tags = soup('span')                         #find <Span> Tag
for tag in tags:
    # Look at the parts of a tag
    print('TAG:', tag)                      #print the Line of Tag
    print('URL:', tag.get('class', None))   #Print Value Of class Or Print None If You Didn't Find Something
    print('Contents:', tag.contents[0])     #print anything after <span>
    ls.append(int(tag.contents[0]))         #store all numbers in list
print('Sum-Contents:', sum(ls))             #sum of this list

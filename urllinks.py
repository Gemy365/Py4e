# download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file
# http://py4e-data.dr-chuck.net/known_by_Jaye.html  Check By this Site

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')                                     #Enter Your URL
html = urllib.request.urlopen(url, context=ctx).read()      #Same as Open To Handle the Data
soup = BeautifulSoup(html, 'html.parser')                   #Work With HTML

# Call all of the anchor tags
tags = soup('a')                    #Search for <a>
for tag in tags:
    print(tag.get('href', None))    #Print Links After href Or Print None If You Didn't Find Something

#Need Comments and Study it again
#Not Compeletly yet.. Try To Enter count = 7 Position = 18 and print the last contents name Start by [B]
# http://py4e-data.dr-chuck.net/known_by_Jaye.html  Check By this Site
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
counter1 = 1
counter2 = 0
url = input('Enter URL- ')                          #Enter URL
cnt = input('Enter Count- ')                        #How Many Times Enter In URLS
pos = input('Enter Position- ')                     #Number Of URL
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
ls = list()
# Retrieve all of the anchor tags
tags = soup('a')                                    #Search for <a>
for tag in tags:
    #print(tag.get('href', None))                    #Print Links After href Or Print None If You Didn't Find Something
    if counter1 == int(pos):
        print('>>>>>>>>>>>>>>>>>OLD>>>>>>>>>>>>>>>>>>>')
        print('OLD' , tags)
    if counter1 == int(pos):
        print('=================NEW===================')
        url = tag.get('href', None)
        print('URL:' , url)
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        tags = soup('a')
        print('New:' , tags)
        counter1 = 0
        counter2 = counter2 + 1
        #if counter2 == int(cnt): break
        #continue
    #   print(tag.get('href', None))                    #Print Links After href Or Print None If You Didn't Find Something
    counter1 = counter1 + 1
    ls.append(tag.contents[0])                      #store all Names in list
print('Contents:', ls[int(pos)-1])                  #list start from index [0] if u wanna fourth name.. [0,1,2,3,4]=> 5 [-1] to get fourth name
print(counter1 , counter2)

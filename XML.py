#Study it again
#http://py4e-data.dr-chuck.net/comments_15164.xml Test It
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET                  #Alias

serviceurl = 'http://py4e-data.dr-chuck.net/comments_15164.xml?'   #URL

while True:
    address = input('Enter location: ')     #address is behind URL.. ex. URL >> [https://translate.google.com/?][hl=ar#en/ar/address%20is%20behind%20URL] << address
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address}) #Compelete The URL
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    #print(data)                                #If U Wanna See The Data
    print('Retrieving', address)                #Print The URL
    print('Retrieved', len(data), 'characters') #How Many Chars of Data
    ls = list()
    tree = ET.fromstring(data)                  #Make It Like Tree
    lst = tree.findall('comments/comment')      #Find All comments/comment
    print('count:' , len(lst))                  #How Many count in This Site
    for item in lst:
        ls.append(int(item.find('count').text)) #Find count Then Get the value
    print('Sum:' , sum(ls))                     #Sum of These Values of counts

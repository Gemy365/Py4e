#Study it again
#http://py4e-data.dr-chuck.net/comments_15165.json Test It
import json
import urllib.request, urllib.parse, urllib.error

serviceurl = 'http://py4e-data.dr-chuck.net/comments_15165.json?'   #URL

while True:
    address = input('Enter location: ')     #address is behind URL.. ex. URL >> [https://translate.google.com/?][hl=ar#en/ar/address%20is%20behind%20URL] << address
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address}) #Compelete The URL
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    count = 0                   #No count found yet
    counter = 0                 #just counter

    print('Retrieving', address)                    #Print URL
    print('Retrieved', len(data), 'characters')     #How Many Chars of Data
    info = json.loads(data)                         #Try To Load all Data
    print('Count:' , len(info['comments']))         #How Many count of this site
    #print(info['comments'])                        #If U Wanna See The Data of comments
    for item in info['comments']:                   #item for Every thing in comments
        count += info['comments'][counter]['count'] #[counter from first count to last count & add them to gether ][Find value of count]
        counter = counter + 1                       #Increase the counter + 1
    print('Sum:' , count)                           #Print The Sum

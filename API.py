#Study it again
#Duke University Test it must get place_id = "ChIJ346g_cT35IcRrbkSoKZwWWo"
import urllib.request, urllib.parse, urllib.error
import json

# Note that Google is increasingly requiring keys
# for this API
serviceurl = 'http://py4e-data.dr-chuck.net/geojson?'   #URL

while True:
    address = input('Enter location: ')     #address is behind URL.. ex. URL >> [https://translate.google.com/?][hl=ar#en/ar/address%20is%20behind%20URL] << address
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address}) #Compelete The URL

    print('Retrieving', url)    #Print URL
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')     #How Many Chars of Data

    try:
        js = json.loads(data)       #Try To Load all Data
    except:
        js = None                   #Otherwise None

    if not js or 'status' not in js or js['status'] != 'OK':    #For AnyError
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js , indent=4))    #[dumps inverse loads][indent for spaces and handling code So try to Change it from 4 to 0,1,2,3 to understand]
    PD = js["results"][0]["place_id"]   #[0 for first 'results' if there are many 'results' and you want the third 'results' Change 0 to 2][Find value of place_id]
    print('P_iD:', PD)                  #print the place_id

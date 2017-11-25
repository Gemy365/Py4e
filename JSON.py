#Need Study it again
import json
# ''' For Multi Lines
data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Chuck"
  }
]
'''
info = json.loads(data)             #read Data And Convert To List
print('User count:', len(info))     #How Many Of Dictionary in the List

for item in info:                   #Every Item In Info
    print('Name', item['name'])     #Print Item Of Name
    print('Id', item['id'])         #Print Item Of ID
    print('Attribute', item['x'])   #Print Item Of X

import re   #Lib Regular Expression

x = 'From: Using the: character'
y = re.findall('^F.+:', x)         #Start Line By [F] & Other Chars To [:]
print(y)

x = 'From: Using the: character'
y = re.findall('^F.+?:', x)         #Start Line By [F] & Other Chars To First [:]
print(y)

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:2:16 2008'
y = re.findall('\S+?@\S+', x)       #series Of Chars include [@] With No Space Right Of Left
print(y)

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:2:16 2008'
y = re.findall('@([^ ]+)', x)       #Print Chars after [@] But without Space
print(y)

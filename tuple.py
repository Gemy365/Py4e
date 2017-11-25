# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")

try:                        #Try To Do This
    if len(fname) < 1 :     #Don't Need To Wite The Name File Just Press Enter
        fname = "mbox-short.txt"
    fopen = open(fname)     #Open File Name

except:                     #If Can't.. Do This
    print("Sorry Your File " + fname + " can't be opened")  #Own Message
    quit()  #Exit From This Program

dic = dict()

for line in fopen:
    if not line.startswith("From "):  #If Line Not Start With This String
        continue                     #Move To Next Line
    words   = line.split()           #Create word As List
    times   = words[5]              #Search On Word Not Chars
    print(times)                    #Print Full Time
    hms  = times.split(":")         #Hour,Minutes,Second like a String
    seconds = hms[0:1]              #Just Store The seconds
    for sec in seconds:
        dic[sec] = dic.get(sec , 0) + 1  #If Exists [own count +1] If not [0 + 1]

tmp = list()

for k,v in dic.items():             #Key & Value Of Dic
    newt = (k,v)                    #New Tuple
    tmp.append(newt)                #Store The Tuple Into The List

for key,value in sorted(tmp):       #Sort The Seconds
    print(key,value)                #Print The Seconds & His Value

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
    words = line.split()             #Create word As List
    emails = words[1:2]              #Search On Word Not Chars
    for email in emails:
        dic[email] = dic.get(email , 0) + 1  #If Exists [own count +1] If not [0 + 1]

bigemail  = None
bigcount  = None

for key,value in dic.items():   #items Take 2 Variables [Key,Value]
    if bigcount is None or value > bigcount:
        bigemail = key
        bigcount = value

print(bigemail , bigcount)  #Print the Biggest Email & His Value
print(dic)                  #To Show All The Dictionary

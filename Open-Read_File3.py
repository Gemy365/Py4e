# Use the file name romeo.txt as the file name
fname = input("Enter file name: ")

try:                        #Try To Do This
    fopen = open(fname)     #Open File Name

except:                     #If Can't.. Do This
    print("Sorry Your File " + fname + " can't be opened")  #Own Message
    quit()  #Exit From This Program

inp = fopen.read()          #Read This File

handle = inp.split()        #Change Str To List

handle.sort()               #Sort It As Alphabetical Order.

lst = list()                #Empty List

for word in handle:         #Search On Every Word In This List
    if not word in lst:     #If Not In Lst
        lst.append(word)    #Add It In The Empty List

print(lst)

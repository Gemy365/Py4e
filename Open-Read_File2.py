# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
count = 0
adding = 0

try:                        #Try To Do This
    fopen = open(fname)     #Open File Name

except:                     #If Can't.. Do This
    print("Sorry Your File " + fname + " can't be opened")  #Own Message
    quit()  #Exit From This Program

for line in fopen:
    if not line.startswith("X-DSPAM-Confidence:"):  #If Line Not Start With This String
        continue                    #Move To Next Line
    count += 1                      #If Found It Increase The Count +1
    index = line.find("0")          #Get The Index of Number Of 0
    adding += float(line[index : ]) #Convert Str To Float And Add Them ToGether

avrage = adding / count             #Get The Average
print("Average spam confidence:" , avrage)

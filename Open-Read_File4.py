# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
count = 0

try:                        #Try To Do This
    if len(fname) < 1 :     #Don't Need To Wite The Name File Just Press Enter
        fname = "mbox-short.txt"
    fopen = open(fname)     #Open File Name

except:                     #If Can't.. Do This
    print("Sorry Your File " + fname + " can't be opened")  #Own Message
    quit()  #Exit From This Program

for line in fopen:
    if not line.startswith("From "):  #If Line Not Start With This String
        continue                    #Move To Next Line
    word = line.split()             #Create word As List
    print(word[1])
    count += 1                      #If Found It Increase The Count +1

print("There were", count, "lines in the file with From as the first word")

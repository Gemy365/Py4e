# Use words.txt as the file name
fname = input("Enter file name: ")     #Ask User To Enter File Name

try:                        #Try To Do This
    fopen = open(fname)     #Open File Name

except:                     #If Can't.. Do This
    print("Sorry Your File " + fname + " can't be opened")  #Own Message
    quit()  #Exit From This Program

inp = fopen.read()      #Read This File

Upper = inp.upper()     #Upper Case

handle = Upper.strip()  #Remove Extra Spaces 

print(handle)

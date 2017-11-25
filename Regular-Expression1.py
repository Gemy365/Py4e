# Use the file name Regular Expression.txt as the file name
import re

fname = input("Enter file name: ")
count = 0

try:                        #Try To Do This
    if len(fname) < 1 :     #Don't Need To Wite The Name File Just Press Enter
        fname = "Regular Expression.txt"
    fopen = open(fname)     #Open File Name

except:                     #If Can't.. Do This
    print("Sorry Your File " + fname + " can't be opened")  #Own Message
    quit()  #Exit From This Program

inp = fopen.read()          #Read This File

ls = list()                 #Empty List

numbers = re.findall('[0-9]+', inp) #Find All Numbers in inp
print(numbers)                      #Print Regular Expression (It Always List of String)
for number in numbers:              #Go through in List
    convert = int(numbers[count])   #Convert list of String to Intger
    ls.append(convert)              #Store Intger in Empty List
    count +=1                       #Incease Count By [1]
print("The count :" , count)       #Count Of Numbers
print("The Sum :"   , sum(ls))     #Find Sum Of Intgers

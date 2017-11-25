x = range(4)        #Create List From 0 To 3

print(x[1])         #Print Index Of 1

Friends = list()    #Create Empty List

Friends.append("Gemy")      #Add In The Empty List
Friends.append("Omar")      #Add In The Empty List
Friends.append("Badr")      #Add In The Empty List

print(Friends)

Letters = ['H' , 'O' , 'A' , 'E' , 'M' , 'D']   #List UnSorted

Letters.sort()  #Sorted List

print(Letters)

Numbers = [17 , 25 , 30 , 5 , 0 , 90 , 47 , 60]

print("Length: " , len(Numbers))

print("Max Number: " , max(Numbers))

print("Min Number: " , min(Numbers))

print("Sum: " , sum(Numbers))

print("Average: " , sum(Numbers) / len(Numbers))

Str = "Hello My Name Is Gemy"   #String

List = Str.split()      #Change Str To List

print(List)

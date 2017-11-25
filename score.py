# Ask User To Enter His Grade
Grade = input("Enter Your Grade Between 0.0 To 1.0 : ")
try:
    g = float(Grade)
except:
    print('Sorry Your Input is Not Number')
    quit()
if (g > 0.0) & (g < 1.0) :
    if g >= 0.9 :
        print('A')
    elif g >= 0.8 :
        print('B')
    elif g >= 0.7 :
        print('C')
    elif g >= 0.6 :
        print('D')
    elif g < 0.6 :
        print('F')
else:
    print('Sorry Your Input is Out Of Range')

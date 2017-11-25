# Get 1.5 For All Employee Work Above 40 Hours & Rate = 10.5
def computepay(h,r): #As A Function
    if h > 40 :
        rph = 40 * r
        extra = (h - 40.0) * (r * 1.5)
        pay = rph + extra
    else :
        pay = h * r
    return pay

hrs = input("Enter Hours: ")    # Enter Hours Like A String
rate = input("Enter Rate: ")    # Enter Rate Like A String
try:    # If Can.. Do It
    h = float(hrs)      # Convert It From String To Float
    r = float(rate)     # Convert It From String To Float
except: # If Can't.. Do It
    print('Error Please Enter Number Only')
    quit()  # Exit From This Code

p = computepay(h,r) #Invoke The Function
print("Pay:",p)

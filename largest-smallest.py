# Ask User To Enter Number Only
largest = None  # There's No Value
smallest = None # There's No Value
while True: # Loop Is True
    num = input("Enter a number: ") # Ask User To Enter Number Or Done
    try:    # If Can.. Do It
        n = int(num)    # Convert It From String To Float
    except: # If Can't.. Do It
        if num == "done" :  # If Input Is "done"
            break   #Out Of While Loop
        else:   #   If Other Thing
            print('Invalid input')  # Message
            continue    # Return To First Line Of While Loop

    if (largest is None) & (smallest is None) :
        largest = n
        smallest = n

    elif largest < n :
        largest = n

    elif smallest > n :
        smallest = n

print("Maximum is", largest)
print("Minimum is", smallest)

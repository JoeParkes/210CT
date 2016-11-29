n = int(input("What is your number?:  ")) # This is for the user to input the data that they want


def perfectsquarenumber(n):
    x = n #this assigns the value of x to n. 
    while True:
        if x**2 <= n: # If x to the power of 2 is equal or less than n then it shall run the following script
            
            print ("The highest perfect square of %s or less is %s" %(n,x**2)) # display's the result

            return x**2 # return the value so that it can be used outside of the function
        else:
            x -= 1
            
perfectsquarenumber(n)
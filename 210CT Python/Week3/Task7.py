n = int(input("What is your number?:  "))

variable = 0
i = 0
for i in range(2,n-1) :

    if((n%i) == 0) :
        variable = variable +1

        break
if(variable == 0) :
    print("This is a prime number");

else :
    print("This is Not a prime number" );

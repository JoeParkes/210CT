# Task 4

Question - Describe thr run time bounds of last weeks task


<b>Code from Task 1 </b>
```
array = [5,2,3,6,1,12]

print "This is the noraml List: - "
print (array)
temp = '0'
lastvalue = 2

temp = array[0]
array[0] = array[lastvalue]
array[lastvalue] = temp

print "This is the changed List: - "
print(array)
    

```
<i>Run time bounds for the code above</i>

<br/>
<br/>

<b>Code from Task 2 </b>

```
x = int(input("What is your number?:  "))

def TrailZero(x):
    Zeros = 0
    for number in range(2, x+1):          
        while number > 0:
            if number % 5 == 0:
                Zeros += 1
                number = number/5
            else:
                break
    return Zeros

print ("Your number has the following number of trailing 0's")
print TrailZero(x)
```
<i>Run time bounds for the code above </i>

The run time bounds for this code show that when x 
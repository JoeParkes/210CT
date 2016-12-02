# Task 12

Question - Write the persudo code for an unweighted graph data structure


<b>Pseudocode from Task 12 </b>
```
CLASS Graph(NODE):
    
    FUNCTION__init__(self):
        self.node = {}
        
    FUNCTION addNode(self, name):
        self.node[name] = node[name]
    
    FUNCTION completedEdge(self, source, target):
        self.node[source] finds the edge and is = to self.node[source] edge + [target of node]

```
<i>Run time bounds for the code above</i>

<br/>
<br/>

<b>Task 12 part 2 - Implementation of the Task above (Task 12) </b>

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
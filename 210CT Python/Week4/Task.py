A = [1,2,3,4,5,6,7,8,9]

def BinarySearch(A, l, u):
    first = 0
    last = len(A)-1
    
    while last > first:
        midpoint = first + (last - first)/2
        if A[midpoint] > l and A[midpoint] < u:
            return True

        elif A[midpoint] < u:
            first = midpoint +1

        elif A[midpoint] > u:
            last = midpoint -1
        
        else:
            return False
 
 
print (("This is the list we are searching from", A))
print BinarySearch(A,1,3)
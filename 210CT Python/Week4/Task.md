```
ARRAY = [1,2,..]

FUNCTION BINARYSEARCH(A, l, u)
    FIRST = 0 
    LAST = len(ARRAY) -1
    
    LOOP WHILE LAST GREATER THAN FIRST:
        Midpoint = FIRST + (LAST-FIRST)/2
    
    IF A[Midpoint] is GREATER THAN l and A[Midpoint] less THAN u:
        RETURN TRUE
    
    ELSE IF A[Midpoint] less THAN u:
        FIRST = Midpoint +1
        
    ELSE IF A[Midpoint] greater than u:
        LAST = midpoint -1
        
    ELSE:
        RETURN FALSE
```
x = 20

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

print TrailZero(x)
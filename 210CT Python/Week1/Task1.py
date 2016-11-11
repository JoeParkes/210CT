

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
def find_odd_integer(arr):
    result = 0
    for n in arr:
        result = result ^ n
    return result

print(find_odd_integer([7])) # should print 7
print(find_odd_integer([0])) # should print 0
print(find_odd_integer([1,1,2])) # should print 2
print(find_odd_integer([0,1,0,1,0])) # should print 0
print(find_odd_integer([1,2,2,3,3,3,4,3,3,3,2,2,1])) # should print 4

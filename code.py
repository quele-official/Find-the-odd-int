def find_odd_integer(arr):
    # Create a hash map to count the number of occurrences of each integer
    counts = {}
    for n in arr:
        if n in counts:
            counts[n] += 1
        else:
            counts[n] = 1
    
    # Iterate over the hash map and return the first key with an odd value
    for n, count in counts.items():
        if count % 2 == 1:
            return n

print(find_odd_integer([7])) # should print 7
print(find_odd_integer([0])) # should print 0
print(find_odd_integer([1,1,2])) # should print 2
print(find_odd_integer([0,1,0,1,0])) # should print 0
print(find_odd_integer([1,2,2,3,3,3,4,3,3,3,2,2,1])) # should print 4

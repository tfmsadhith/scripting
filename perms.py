# Sanjay Adhith 2024.

# Singapore, Hillview

# A script to test out the ideas in Knuth's
# Art of Computer Programming 1.2.5.

# This first method is I guess what you may
# call the naive method. Just shove in the
# new element in all the possible places where
# it can be shoved in.

def method_one(permutation, element):
    collection = []
    for i in range(len(permutation) + 1):
        temp = permutation.copy()
        temp.insert(i, element)
        collection.append(temp)
    return collection

# This second method is described by Knuth
# in his book.

# I can't fathom why anyone would want
# to use this method. Perhaps will Knuth
# will elucidate this matter in a later
# volume.

# I'm just implementing it to save me
# the pain of manually tracing it for
# an exercise in his book.

def method_two(permutation, element):
    return 0

def permute(objects):
    perms = [[]]
    for i in objects:
        temp_perms = []
        for j in perms:
            temp_perms += method_one(j,i)
        perms = temp_perms
    return perms

objects = [1,2,3]
for i in range(len(objects) + 1):
    new_objects = objects.copy()
    new_objects.append(1/2 + i)
    print(new_objects)

# Ordering the list cannot be done
# faster than sorting because if it
# could then we would have a faster
# method for sorting.
    
def ordering(fractional):
    sorted_fractional = sorted(fractional.copy())
    temp = []
    for i in fractional:
      temp.append(sorted_fractional.index(i))
    return temp

print(ordering([2,3,1,0.5]))

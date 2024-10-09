# Sanjay Adhith

# Singapore, Hillview

# https://en.wikipedia.org/wiki/Cyclic_permutation

# This is useful if you're doing a combinatorics, group
# theory or elementary number theory class. But really you
# should just get good at working with this notation in your
# head. 

top_row = [1,2,3,4,5,6]
bottom_row = [3,5,6,4,2,1]

assert len(top_row) == len(bottom_row)

def get_cycle(top_row, bottom_row):
    cycle = []
    current = top_row[0]
    while current not in cycle:
        cycle.append(current)
        current = bottom_row[top_row.index(current)]
    return cycle

def cycle(top_row, bottom_row, toggle=0):
    decomp = []
    current = []
    while top_row: # Supposedly this is more "Pythonic".
        current = get_cycle(top_row, bottom_row)
        for i in current:
            bottom_row.remove(bottom_row[top_row.index(i)])
            top_row.remove(i)
        decomp.append(current)

    # Remove 1-cycles from cycle decompositions
    for i in range(toggle):
        decomp = list(filter(lambda x : len(x) > 1, decomp))
    return decomp

decomp = cycle(top_row, bottom_row, 0)
        
# Can you go back to the top and bottom row format from the cycle decompositions?
# Well if you eliminate the 1-cycles this can't be done (unless the top or bottom
# row is provided).

# However, if you include the 1-cycles, then sure it can be done.

def unfold_cycle(cycle):
    cycle.append(cycle[0])
    return cycle
    
def cycle_recomp(decomp):
    recomped = []
    for i in decomp:
        recomped.append(unfold_cycle(i))

    top_row = []
    bottom_row = []

    for recomp in recomped:
        for i in range(len(recomp) - 1):
            top_row.append(recomp[i])
            bottom_row.append(recomp[i + 1])

    return [top_row, bottom_row]
        
cycle_recomp(decomp)

# Further reading: https://math.mit.edu/~fgotti/docs/Courses/Combinatorial%20Analysis/11.%20Permutations%20I/Permutations%20I.pdf

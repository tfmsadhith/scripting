 # Sanjay Adhith

# Singapore, Hillview

# First, we implement a naive and stupid way to do
# cardinality estimation

# https://www-cs-faculty.stanford.edu/~knuth/papers/cvm-note.pdf

A = ['a', 'b', 'c', 'd', 'e', 'f', 'b', 'i', 'l', 'l', 'c', 1, 2, 3, 3, 3, 3, 3, 3,5, 6, 7, 8, 9, 10, 11, 12, 13, 11, 1099, 121]
print(len(A))
print(len(set(A)))
def naive(A):
    buffer = []
    for i in A:
        if i not in buffer:
            buffer.append(i)
    return len(buffer)

print(naive(A))

# Now let's implement the algorithm on the first page
# Knuth never says this explicitly, but we are given the
# length of the stream as $m$.

from random import uniform

def algorithm_d(stream, s):
    m = len(stream) # We assume that this is given to us in advance.
    t = -1 # Note that Knuth indexes the stream from 1. 
    p = 1
    a = 0
    buffer = []
    while t < (m - 1):
        t += 1
        a = stream[t]
        u = uniform(0,1)
        buffer = list(filter(lambda x : x[1] != a, buffer)) 
        if u < p:
            if (len(buffer) < s):
                buffer.append([u, a])
            else:
                buffer = sorted(buffer)
                p = max(buffer[-1][0],u)
                buffer.pop()
                buffer.append([u, a])
    return len(buffer) / p 

print(sorted([[1.34,12], [2.123,3], [3,6]]))
sum = 0
runs = 1000
for i in range(0, runs):
    sum += algorithm_d(A, 10)

print(sum/runs)


# This is the algorithm that CVM originally published. Let's find
# some flaws in it.
def algorithm_x(stream, s):
    m = len(stream)
    t = -1
    p = 1
    buffer = []
    while t < m - 1:
        t += 1
        a = stream[t]
        u = uniform(0,1)
        buffer = list(filter(lambda x : x != a, buffer)) 
        if u < p:
            buffer.append(a)
        if len(buffer) == s:
            buffer = list(filter(lambda x : uniform(0,1) >= 1/2, buffer))
            p /= 2
            if len(buffer) == s:
                return "FAILED"
        
    return len(buffer)/p

sum = 0
runs = 30000
for i in range(0, runs):
    sum += algorithm_x(A, 4)

print(sum/runs)

# I can't see a difference between this and Knuth's algorithm for this
# example at least.

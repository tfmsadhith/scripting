# Sanjay Adhith

# Singapore, Hillview

# The goal is to generate a random permutation.

import random 

def shuffle(n):
    numbers = list(range(n))
    shuffled = []
    while len(numbers) != 0:
        k = random.randint(0, len(numbers) - 1)
        shuffled.append(numbers[k])
        numbers.pop(k)
    return shuffled
    

print(shuffle(10))

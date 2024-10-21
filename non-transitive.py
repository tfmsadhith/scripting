# Sanjay Adhith

# 21 October 2024

# Knuth Volume 4b MPR

import itertools

A = [5,1,5,5,1,5]
B = [4,3,4,4,3,6]
C = [3,2,3,6,2,6]

store = []
for i in range(1,6 + 1):
    for j in range(6):
        store.append(i)

print(store)

unique_die = list(set(itertools.combinations(store, 6)))

print(len(unique_die))

def X_gt_Y(X, Y):
    count = 0
    total = 0
    for i in X:
        for j in Y:
            if i > j:
                count += 1
            total += 1
    return (count / total) > 0.55556


def check_triplet(triplet):
    return X_gt_Y(triplet[0], triplet[1]) and X_gt_Y(triplet[1], triplet[2]) and X_gt_Y(triplet[2], triplet[0])


def strict(X, Y):
    count = 0
    total = 0
    for i in X:
        for j in Y:
            if i > j:
                count += 1
            total += 1
    return (count/total) 


possible_candidates = list(filter(check_triplet, list((itertools.combinations(unique_die, 3)))))

for i in possible_candidates:
    print(i, strict(i[0], i[1]), strict(i[1], i[2]), strict(i[2], i[0]))


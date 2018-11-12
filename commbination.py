import itertools
la = [1, 2, 3, 4, 5]
print(len(la))
for i in range(1, len(la)+1):
    print("combination of {} numbers in {}".format(i, la))
    for j in itertools.combinations(la, i):
        print(j)

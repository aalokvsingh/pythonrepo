from __future__ import print_function
num = int(input("enter number of rows"))
for i in range(0, num):
    for j in range(0, i):
        print(" ", end=" ")
    for k in range(num-i, 0, -1):
        print("*", end=" ")
    print()
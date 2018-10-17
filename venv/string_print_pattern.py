from __future__ import print_function
name = raw_input("enter name")
length = len(name)
for i in range(0, length):
    for j in range(0, i+1):
        print(name[i], end=" ")
    print()
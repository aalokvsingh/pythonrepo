# This program is to print * from right

from __future__ import print_function

num =5
z = num
# to create row
for i in range(0,num):
    # to create column fron space
    for j in range(0,z-1):
        print(" ", end=" ")
    # to create column for *
    for k in range(0,i):
        print("* ",end="")
    z -= 1
    print("\r")

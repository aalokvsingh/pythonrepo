# Print number pattern in python using loop and range function
# We need to use two loop to print this pattern technically called nested loop
# Outer loop is used to handle number of rows and inner loop is used to handle number of columns
# inner loop iteration depends on value of outer loop
# add new line after each row iteration
# output example 1
# 1
# 2 2
# 3 3 3
# 4 4 4 4


from __future__ import print_function
num = 5
# outer loop to iterate number of rows
for i in range(num):
    # inner loop to iterate number of columns and value to print in each column depend upon outer loop value
    for j in range(i):
        print(i,end="")
    # Add new line after each row iteration
    print("\r")

print("===================================================\n")
print("Number Patter Example 2\n")

# output
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for i in range(0,num):
    for j in range(1,i):
        print(j, end="")
    print("\r")

print("===================================================\n")
print("Number Patter Example 3\n")
# outout
# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1

for i in range(0,num):
    # print("rows: ")
    # print(i)
    for j in range(i,0,-1):
        print(j,end="")
    print("\r")

print("===================================================\n")
print("Number Patter Example 4\n")

#   1
#    2    1
#    4    2    1
#    8    4    2    1
#   16    8    4    2    1
#   32   16    8    4    2    1
#   64   32   16    8    4    2    1
#  128   64   32   16    8    4    2    1

for i in range(1,num):
    # print("rows: ")
    # print(i)
    for j in range(i-1,-1,-1):
        # x**y (x to the power y)
        print(2**j, end=' ')
    print("\r")


print("===================================================\n")
print("Number Patter Example 5\n")

for i in range(1, num):
    for i in range(0, i, 1):
        print(2**i, end=' ')
    for i in range(-1+i, -1, -1):
        print(2**i, end=' ')
    print("")

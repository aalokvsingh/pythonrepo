num = int(input("enter a number "))
for i in range(2, num+1 ):
    if num % i == 0:
        print("this is not a prime number")
        print (num, "is",num//i,"times", i)

    else
        print("it is prime number")
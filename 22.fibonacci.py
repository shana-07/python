n = int(input("enter the number of terms: "))

a, b = 0, 1
if n<=0:
        print("please enter a positive number:")
elif n == 1:
    print("fibonacci series up to",n,"terms:")
    print(a)
else:
    print("fibonacci sequence:")
    for i in range(n):
        print(a, end=" ")
        c= a+b
        a=b
        b=c

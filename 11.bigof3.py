num1 = float(input("enter first number:"));
num2 = float(input("enter second number:"));
num3 = float(input("enter third number:"));

if num1>=num2 and num1>=num3:
             biggest= num1
elif num2>=num3 and num2>num1:
    biggest = num2
else:
    biggest= num3

print("the biggest number is:",biggest)



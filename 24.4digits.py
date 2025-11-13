import math
result = []

for num in range(1000,10000):
    root = int(math.sqrt(num))
    if root*root==num:
        digits = str(num)
        if all(int(d) % 2 == 0 for d in digits):
            result.append(num)

print("four digit perfect squares with all even digits:")
print(result)

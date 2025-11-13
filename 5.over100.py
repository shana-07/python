numbers = input("enter a list of integers separated by spaces: ").split()
numbers=[int(num) for num in numbers]
result = [num if num <= 100 else 'over' for num in numbers]
print("\nModified list:")
print(result)

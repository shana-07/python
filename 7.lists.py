list1 = list(map(int, input("enter numbers for list 1(seperated by spaces):").split()))
list2 = list(map(int, input("enter numbers for list 2(seperated by spaces):").split()))
if len(list1) == len(list2):
    print("\n(a) both lists are of same length")
else:
    print("\n(a) lists are different length.")

if sum(list1)== sum(list2):
    print("(b) both list have the same sum.")
else:
    print("(b) list have different sum.")

common_values=set(list1) & set(list2)
if common_values:
    print("(c) common values in both lists:",common_values)
else:
    print("(c) no common values found.")

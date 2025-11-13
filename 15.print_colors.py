color_list1 = input("enter colors for list 1(seperated by spaces):").split();
color_list2 = input("enter colors for list 1(seperated by spaces):").split();

unique_colors = [color for color in color_list1 if color not in color_list2]

print("\nColors present in list1 but not in list2:");
print(unique_colors)

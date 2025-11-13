my_dict ={'c':3,'a':1,'b':2}

ascending = dict(sorted(my_dict.items()))
print("ascending order:",ascending);

descending = dict(sorted(my_dict.items(),reverse=True))
print("descending order:",descending);

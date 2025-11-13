string = input("enter the string: ");
first_char = string[0]
modified_string = first_char+string[1:].replace(first_char,'$')
print("modified string:",modified_string)

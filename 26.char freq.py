string = input("enter a string:")
freq={}
for char in string:
    if char in freq:
        freq[char]+=1
    else:
        freq[char] = 1

print("character frequency:")
for key, value in freq.items():
    print(key, ":",value)

# looping over characters in a string

str1 = "HYDERABAD"
for ch in str1:
    print(ch, end=" ")
print()
   
str2 = "AMARAVATI"
length = len(str2)
i = 0
while i < length:
    print(str2[i], end=" ")
    i += 1

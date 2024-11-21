x = input("Enter a value: ")
y = input("Enter another value: ")

print(x + y)        # '123456'

print(type(x))      # <class 'str'>
print(type(y))      # <class 'str'>

x
'123'
y
'456'

# int(value) -> converts the value to an interger. The value shouldn't contain non-numeric characters.

x = input("Enter a value: ")
Enter a value: 123
x
'123'

x = int(x)
x
123

y = input("Enter another value: ")
Enter another value: 456

y
'456'

y = int(y)
y
456

x + y
579

# chaining functions

x = int(input("Enter a value: "))
Enter a value: 111
x
111

type(x)
<class 'int'>

y = int(input("Enter another value: "))
Enter another value: 444

x + y
555

# BASIC STRING METHODS

# 1. isalpha()
# returns True if all characters in the string are letters
str1 = "Hello"
str2 = "Hello123"
str3 = "Hello!"
str4 = "Hello world"

print("ISALPHA()")
print(str1.isalpha())  # True
print(str2.isalpha())  # False
print(str3.isalpha())  # False
print(str4.isalpha())  # False
print()

# 2. islower()
# returns True if all letters are in lowercase
str5 = "hello"
str6 = "Hello"
str7 = "HELLO"
str8 = "hello world"
str9 = "hello123"
print("ISLOWER()")
print(str5.islower())  # True
print(str6.islower())  # False
print(str7.islower())  # False
print(str8.islower())  # True
print(str9.islower())  # True
print()

# 3. isupper()
# returns True if all letters are in uppercase
str10 = "HELLO"
str11 = "Hello"
str12 = "hello"
str13 = "HELLO WORLD"
str14 = "HELLO123"
print("ISUPPER()")
print(str10.isupper())  # True
print(str11.isupper())  # False
print(str12.isupper())  # False
print(str13.isupper())  # True
print(str14.isupper())  # True
print()

# 4. isdigit()
# returns True if all characters are digits
str15 = "123"
str16 = "123abc"
str17 = "abc"
str18 = "123 456"
print("ISDIGIT()")
print(str15.isdigit())  # True
print(str16.isdigit())  # False
print(str17.isdigit())  # False
print(str18.isdigit())  # False
print()

# 5. startswith(value)
# returns True if the string starts with the specified value
str19 = "Hello, world!"
print("STARTSWITH()")
print(str19.startswith("Hello"))  # True
print(str19.startswith("hello"))  # False
print(str19.startswith("world"))  # False
print()

# 6. endswith(value)
# returns True if the string ends with the specified value
str20 = "Hello, world!"
print("ENDSWITH()")
print(str20.endswith("world!"))  # True
print(str20.endswith("world"))  # False
print(str20.endswith("Hello"))  # False
print()

# 7. lower()
# returns the string in lowercase
str21 = "Hello, World!"
print("LOWER()")
print(str21.lower())  # hello, world!
print()

# 8. upper()
# returns the string in uppercase
str22 = "Hello, World!"
print("UPPER()")
print(str22.upper())  # HELLO, WORLD!
print()

# 9. title()
# returns the string in title case
str23 = "hello, world!"
print("TITLE()")
print(str23.title())  # Hello, World!
print()

# 10. lstrip()
# returns a left trim version of the string
str24 = "   Hello, world!   "
print("LSTRIP()")
print(str24.lstrip())  # Hello, world!
print()

# 11. rstrip()
# returns a right trim version of the string
str25 = "   Hello, world!   "
print("RSTRIP()")
print(str25.rstrip())  #    Hello, world!
print()

# 12. strip()
# returns a trimmed version of the string
str26 = "   Hello, world!   "
print("STRIP()")
print(str26.strip())  # Hello, world!
print()

# 13. ljust(width)
# returns a left justified version of the string
str27 = "Hello"
print("LJUST()")
print(str27.ljust(10, "-"))  # Hello-----
print()

# 14. rjust(width)
# returns a right justified version of the string
str28 = "Hello"
print("RJUST()")
print(str28.rjust(10, "-"))  # -----Hello
print()


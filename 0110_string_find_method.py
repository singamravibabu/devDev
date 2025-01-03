# find(sub_str[, start[, end]]) method
# Return the lowest index in the sub_str

str1 = "Python is a programming language"

sub_str1 = "is"
sub_str2 = "hello"

print("is index:", str1.find(sub_str1)) # 7
print("hello index:", str1.find(sub_str2)) # -1

email = "kiran.kumar@gmail.com"
at_index = email.find("@")
dot_index = email.find(".", at_index + 1)
print("at index:", at_index) # 11
print("dot index:", dot_index) # 17

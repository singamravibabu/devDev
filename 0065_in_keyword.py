# using 'in' keyword with list object
# 'in' keyword is a membership operator
# it checks if a value is present in a list or not
# it returns True if value is present in list
# it returns False if value is not present in list
# Syntax: item in list

# list of employees
emps = ['John', 'David', 'Mike', 'Sam', 'Tom']

# check if 'Mike' is a member of emps list
print('Mike' in emps)
print('Anand' in emps)

if 'John' in emps:
    print("Call John for the meeting.")

if 'Praveen' in emps:
    print("Call praveen to join the meeting.")
else:
    print("Praveen isn't an employee.")
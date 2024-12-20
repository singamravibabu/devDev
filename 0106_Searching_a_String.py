# searching a string
# Syntax: term in string
# Syntax: sub_string in larger_string
# If sub_string is part of larger_string, it returns True
# If sub_string is not part of larger_string, it returns False

# example
msg = "Congratulations. You have won a million dollars"
print("won" in msg)
print("tion" in msg)
print("lose" in msg)

if "won" in msg:
    print("You are a winner")
else:
    print("You are a loser")

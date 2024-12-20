# formatting numbers using f-strings
# formatting specification mini-language
# :[fill][align][sign][#][0][width][grouping_option][.precision][type]
# :[width][comma][.deci_places][type]
# [type]:   d (integer), f (float), e (scientific), % (percentage)
# alignment: < (left), > (right), ^ (center)

x = 12345.6789
y = 0.123456789

# :[width]
print(f"{x}")
print(f"{x:20}")    # 20 characters wide
print(f"{x:16}")    # 16 characters wide
print(f"{x:<16}")   # left aligned
print(f"{x:^16}")   # center aligned


# :[width][comma]
print(f"{x:20,}")   # 20 characters wide with comma
print(f"{x:,}")     # comma separator

# :[width][comma][.deci_places]
print(f"{x:20,.3}")     # 20 characters wide with comma and 3 decimal places
print(f"{x:20,.3f}")    # 20 characters wide with comma and 3 decimal places
print(f"{x:20,.1f}")    # 20 characters wide with comma and 1 decimal place
print(f"{x:20,.2f}")    # 20 characters wide with comma and 2 decimal places

# :[width][comma][.deci_places][type]
print(f"{y}")           # default
print(f"{y:.2%}")       # percentage with 2 decimal places
print(f"{y:.4%}")       # percentage with 4 decimal places
print(f"{y:.3%}")       # percentage with 3 decimal places

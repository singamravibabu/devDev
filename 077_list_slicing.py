# list slicing
# list[start:end:step]

values = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
upto_25 = values[:5]
print("Upto 25: ", upto_25)
numbers_ending_in_5 = values[0::2]
print("Numbers ending in 5: ", numbers_ending_in_5)
numbers_ending_in_0 = values[1::2]
print("Numbers ending in 0: ", numbers_ending_in_0)
fifteen_multiples = values[2::3]
print("Fifteen multiples: ", fifteen_multiples)
reverse_values = values[::-1]
print("Reverse values: ", reverse_values)
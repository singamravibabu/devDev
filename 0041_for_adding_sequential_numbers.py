numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total_numbers = 0

five_multiples = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
total_five_multiples = 0

for value in numbers:
    total_numbers += value

print(f"Total numbers: {total_numbers}")

for value in five_multiples:
    total_five_multiples += value

print(f"Total of five multiples: {total_five_multiples}")
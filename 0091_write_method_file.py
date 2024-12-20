# the write() method of the file object
# write() method is used in write and append modes
# Syntax: file.write(string)

years = [2020, 2021, 2022, 2023, 2024]

# writing to a file
with open("years.txt", "w") as file:
    for year in years:
        file.write(str(year) + "\n")

new_years = []
# reading from a file
with open("years.txt", "r") as file:
    content = file.readlines()
    for year in content:
        year = year.replace("\n", "")
        year = int(year)
        new_years.append(year)
print(new_years)
        
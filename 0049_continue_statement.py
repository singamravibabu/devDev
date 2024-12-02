salaries = [55000, 84000, 29000, 44000, 102000, 50000, 33000, 15000]

# prints only four salaries
for salary in salaries:
    if salary >= 100000:
        break
    print(salary)


# prints five salaries
for salary in salaries:
    print(salary)
    if salary >= 100000:
        break
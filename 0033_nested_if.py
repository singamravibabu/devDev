EDU = 'mba'
EXP = 3

education = input("Qualification (lower): ")
experience = int(input("Years of experience: "))

if education == EDU and experience >= EXP:
    print("You are eligible to apply for the job!")
else:
    if education == EDU and experience < EXP:
        print("You are an MBA, but you don't have experience.")
    elif education != EDU and experience >= EXP:
        print("You have experience, but not qualified.")
    else:
        print("You are neither an MBA and nor experienced.")
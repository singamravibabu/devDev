# doing samething using for and while loops

scores = [50, 60, 70, 80, 90, 100]
total = 0
for score in scores:
    total += score
print(total)


total = 0
i = 0
while i < len(scores):
    total += scores[i]
    i += 1
print(total)
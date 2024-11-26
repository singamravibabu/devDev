score = -5

if score >= 90 and score <= 100:
    print("Grade A")
elif score >= 80 and score < 90:
    print("Grade B")
elif score >= 70 and score < 80:
    print("Garde C")
elif score >= 60 and score < 70:
    print("Grade D")
elif score >= 50 and score < 60:
    print("Grade E")
elif score >= 0 and score < 50:
    print("Fail")
else:
    print(f"Result: {score} not a valid score.")

# statement(s)
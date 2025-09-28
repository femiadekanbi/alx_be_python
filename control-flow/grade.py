marks = int(input("Enter your score: "))
if marks >= 80:
    print("Distinction")
elif marks >= 70:
    print("Excellent")
elif marks < 50:
    print("Pass")
else:
    print("Fail")
.:
print("Invalid input")

print(f"Your total score is {marks}. Any alterations renders this result invalid")
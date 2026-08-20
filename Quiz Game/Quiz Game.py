score = 0

answer1 = input("What is the capital of France? ")
if answer1.strip().lower() == "paris":
    score += 1
    print("Correct!")
else:
    print("Wrong! The correct answer was Paris.")

answer2 = input("What is 5 + 7? ")
if answer2.strip().lower() == "12":
    score += 1
    print("Correct!")
else:
    print("Wrong! The correct answer was 12.")

answer3 = input("What is the largest planet in our solar system? ")
if answer3.strip().lower() == "jupiter":
    score += 1
    print("Correct!")
else:
    print("Wrong! The correct answer was Jupiter.")

print(f"\nYour final score: {score}/3")
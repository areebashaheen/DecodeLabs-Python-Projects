total = 0

while True:
    expense = input("Enter expense (or 'quit' to stop): ")
    
    if expense == "quit":
        break
    
    try:
        expense = int(expense)
        total += expense
    except ValueError:
        print("Invalid input, please enter a number")

print("Total Spent:", total)
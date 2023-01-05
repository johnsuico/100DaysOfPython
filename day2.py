# Goal: To create a tip calculator.
# Ask for the total bill price.
# Ask how many people to split the bill.
# Ask the tip percentage.
# Calculate how much each person should pay.

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?\n"))
people = int(input("How many people to split the bill?\n"))
tipPercentage = int(input("What percentage tip would you like to give? 10, 12, or 15?\n")) / 100
tipCalc = bill * tipPercentage
finalBill = bill + tipCalc
perPerson = finalBill / people

print("Each person will pay: $" + str(round(perPerson, 2)))
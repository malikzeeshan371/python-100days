# Greeting
print("Welcome to the tip claculator.")

# taking input and changing the data types according to our requirement
bill = float(input("What was the total bill ? $"))
tip = int(input("What percentage tip would you like to give ? 10,12 or 15 %"))
people = int(input("How many people to split the bill ?"))

# calculating the bill with tip 
bill_with_tip = tip / 100 * bill + bill

# calculating bill per person
bill_per_person = (bill + tip) / people


# making the bill per person with 2 decimal point
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay ${final_amount}")
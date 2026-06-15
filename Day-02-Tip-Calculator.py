# print("Welcome to the tip calculator!")
# bill = float(input("What was the total bill? $"))
# tip = int(input("What percentage tip would you like to give? 10 12 15 "))
# people = int(input("How many people to split the bill? "))

print("Welcome to the tip calculator")
bill= float(input("What was the total bill? $"))
tip= int(input("What percentage tip would you like to give? 10/12/15\n"))
people = int(input("How many people to split the bill?\n"))

# bill_with_tip= tip /100 * bill + bill
tip= tip /100 * bill
total_bill= bill + tip
bill_per_person= total_bill / people

print(f"Each person should pay:$ {bill_per_person} ")




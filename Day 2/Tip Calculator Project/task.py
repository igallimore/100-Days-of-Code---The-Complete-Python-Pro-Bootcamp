#total of bill
#percentage of tip 10, 15 or 20
#how many people to split the bill with

print("Welcome to the tip calculator! Let's get started!")

total_bill = input ("What is the total of the bill? ")
tip_percent = input ("How much do you want to tip? 10, 15 or 20 percent? ")
total_people = input ("How many people will be splitting this bill? ")

tip_percent = int(tip_percent)
total_bill = float(total_bill)
print(total_bill)
total_bill = round(total_bill, 2)
print(total_bill)
total_people = int(total_people)
the_tip = tip_percent / 100
print(the_tip)
the_complete_tip = total_bill * the_tip
the_total = total_bill + round(the_complete_tip, 2)

print(f"Here is the total: ${the_total}")
print (f"Everyone gets to pay: ${round(the_total / total_people, 2)}")










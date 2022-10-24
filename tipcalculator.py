print("Welcome to the tip calculator!")

bill_amount = int(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? 10, 12 or 15: "))
ppl = int(input("How many people to split the bill?: "))
tip_amount = bill_amount * (tip_percentage/100)
bill_payment =float((tip_amount+bill_amount)/ppl)
print(bill_payment)
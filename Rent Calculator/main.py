## input we need from the user
# total rent
# total food ordered for snacking
# electricity units spend
# charge per unit
# persons living in room/flat


# #output
# Total amount you've to pay is


rent = float(input("Enter your hostel/flat  rent: "))

food = float(input("Enter the amount of food ordered = "))

electricity_spend = float(input("Enter the total of electricity spend: "))

charge_per_unit = int(input("Enter the charge per unit = "))
persons = int(input("Enter the number if persons living in room/flat = "))

total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) // persons

print("Each person will pay = ",output)
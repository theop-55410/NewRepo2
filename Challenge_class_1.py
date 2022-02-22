
#container for different loans
loan_costs = [500, 600, 200, 1000, 450]
#the amount of loans
total_loans = len(loan_costs)
#the total of all the loans
loan_total = sum(loan_costs)
#mean loan price
avg_loan_price = loan_total / total_loans
#prints all values
print(f"There were {total_loans} loans in the list. They amounted to ${loan_total}. The average loan price was {avg_loan_price}")

#print(loan_costs.get([1]))


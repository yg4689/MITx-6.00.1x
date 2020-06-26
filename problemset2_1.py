# Problem 1 - Paying Debt off in a Year
# Write a program to calculate the credit card balance after one year if a person only
# pays the minimum monthly payment required by the credit card company each month.
#
# The following variables contain values as described below:
#
# balance - the outstanding balance on the credit card
#
# annualInterestRate - annual interest rate as a decimal
#
# monthlyPaymentRate - minimum monthly payment rate as a decimal
#
# For each month, calculate statements on the monthly payment and remaining balance.
# At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy

monthly_intrest=annualInterestRate/12
for i in range(12):
    minimumpayment=(balance*monthlyPaymentRate)
    ub=balance-minimumpayment
    balance=(monthly_intrest* ub)+ub
print(round(balance,2))
# Problem 3 description:
# Write a program using bisection search to calculate a more accurate fixed monthly payment than we did in Problem 2 without running into the problem of slow code.
# The following variables contain values as described below:
# balance - the outstanding balance on the credit card
# annualInterestRate - annual interest rate as a decimal

# To recap the problem: we are searching for the smallest monthly payment such that we can pay off the entire balance within a year. 
# What is a reasonable lower bound for this payment value? $0 is the obvious answer, but you can do better than that. 
# If there was no interest, the debt can be paid off by monthly payments of one-twelfth of the original balance, so we must pay at least this much every month. 
# One-twelfth of the original balance is a good lower bound.

# What is a good upper bound? Imagine that instead of paying monthly, we paid off the entire balance at the end of the year. 
# What we ultimately pay must be greater than what we would've paid in monthly installments, because the interest was compounded on the balance we didn't pay off each month. 
# So a good upper bound for the monthly payment would be one-twelfth of the balance, after having its interest compounded monthly for an entire year.

# In short:
# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly payment lower bound = Balance / 12
# Monthly payment upper bound = (Balance x (1 + Monthly interest rate)12) / 12.0

# Write a program that uses these bounds and bisection search (for more info check out the Wikipedia page on bisection search) to find the smallest monthly payment to the cent (no more multiples of $10) such that we can pay off the debt within a year. 
# Try it out with large inputs, and notice how fast it is (try the same large inputs in your solution to Problem 2 to compare!). 
# Produce the same return value as you did in Problem 2.

# Solution:
def LowestPayment(balance,annualInterestRate):
    
    monthInterestRate = annualInterestRate / 12
    lower_bound = balance / 12
    upper_bound = (balance * (1 + monthInterestRate) ** 12) / 12
    
    while balance > 0:
        unpaid = balance
        month_payment = (lower_bound + upper_bound) / 2
        
        for i in range(12):
            unpaid = (unpaid - month_payment) * (1 + monthInterestRate)
        if unpaid > 0 :
            lower_bound = month_payment
        elif unpaid < -0.01:
            upper_bound = month_payment
        else:
            break

    
    print ('Lowest Payment: ', '%0.2f' % month_payment)

LowestPayment (balance,annualInterestRate)

# Test Case 1:
# balance = 320000
# annualInterestRate = 0.2
# Result above Code Generate:
# Lowest Payment: 29157.09

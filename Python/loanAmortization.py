'''
Program: Loan Amortization
Date: 6/10/16
Name: Harry Brown III
'''

def payment(loan, years, APR):
    # calculate interest rate per month
    M = years *12
    P = APR/100
    R = P/M
    J = 1 - (1 + R) ** -M
    IR = R * loan

    #calculate monthly payment
    mPay = IR/J

    #calculate total payment with interest
    tPay = mPay * M
    return(M, P, R, J, mPay, tPay)

def rate(loan, years, APR, R, mPay):
    # calculate interest rate per month
    IR = R * loan
    
    #calculate principal
    PR = mPay - IR

    #calculate balance
    B = loan - PR
    return(IR, PR, B)

#get user input
loan = eval(input('Enter the loan amount: '))
years = eval(input('Enter number of years as an integer: '))
APR = eval(input('Enter yearly interest rate: '))

#call payment function
M, P, R, J, mPay, tPay = payment(loan, years, APR)

#display output
payment = print('Monthly payment: ' + str(format(mPay, '.2f')))
total = print('Total payment: ' + str(format(tPay, '.1f')) + '\n')

print('Payment#\t' + 'Interest\t' + 'Principal\t' + 'Balance')
for x in range(1, M+1):
    #call rate function
    IR, PR, B = rate(loan, years, APR, R, mPay)
    
    #output payment, interest, principal, and balance
    print(str(x) + '\t\t' + str(format(IR, '.2f')) + '\t\t' + \
          str(format(PR, '.2f')) + '\t\t' + str(format(B, '.2f')))
    
    #assign balance as the remaining loan amount
    loan = B

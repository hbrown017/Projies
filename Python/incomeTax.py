'''
Name: Harry Brown III
Program: Income Tax Calculator
Date: 6/15/16
'''

def statusIteration(amount, status, option, plus):
    iteration = 0
    if amount <= status[option][1]: #15%
        iteration = 2
    elif amount <= status[option][2]: #25%
        iteration = 3
    elif amount <= status[option][3]: #28%
        iteration = 4
    elif amount <= status[option][4]: #33%
        iteration = 5
    else:   #35%
        iteration = 5
        plus = True
    return(iteration, plus)

def allOption(rates, status, index, tax, amount, option):
    plus = False
    #10% marginal tax rate
    if amount <= status[option][0]:
        tax = amount * rates[0]
        return(tax)
    else:
        tax = status[option][index] * rates[index]
        iteration, plus = statusIteration(amount, status, option, plus)
        tax += (amount - status[option][index]) * rates[index+1]
    return(tax)

def main():
    index = 0
    tax = 0
    #taxable rate
    rates = [0.10, 0.15, 0.25, 0.28, 0.33, 0.35]

    #filing status rates
    status = [[8350, 33950, 82250, 171550, 372950],
          [16700, 67900, 131050, 208850, 372950],
          [8350, 33950, 68525, 104425, 186475],
          [11950, 45500, 117450, 190200, 372950]]

    
    #input income amount and option (0, 1, 2 ,3)
    amount = eval(input('Enter your income amount: '))
    print('\nSingle = 0' + '\t' + 'Joint = 1' + '\n' + \
          'Seperated = 2' + '\t' + 'Household = 3' + '\n')
    option = eval(input('Enter an option (0/1/2/3): '))
    
    tax = allOption(rates, status, index, tax, amount, option)
    print('Your tax is: ' + str(tax))
 
#call main function
main()

'''
Name: Harry Brown III
Program: Payroll Calculator
Date: 6/6/2016
'''

# get users input
name = input("Enter employee's name: ")
hours = eval(input("Enter number of hours worked in a week: "))
rate = eval(input("Enter hourly pay rate: "))
Ftax = eval(input("Enter federal tax witholding rate: "))
Stax = eval(input("Enter state tax withholding rate: "))

#compute gross pay including overtime
if hours > 40:
    overtime = hours - 40
    gross = 40 * rate + overtime * 1.5 * rate
else:
    gross = hours * rate

#perform calculations
fHolding = gross * Ftax
sHolding = gross * Stax
deduction = fHolding + sHolding
pay = gross - deduction

#concatinate strings
out = "\n\nEmployee Name: " + name + '\n\n'
out += "Hours Worked: " + str(hours) + '\n'
out += "Pay Rate: $" + str(rate) + '\n'
out += "Gross Pay: $" + str(gross) + '\n'
out += "Deductions: \n"
out += " Federal Withholding(" + str(Ftax * 100) + \
       "%): $" + str(int(fHolding * 100) / 100.0) + '\n'
out += " State Withholding(" + str(Stax * 100) + \
       "%): $" + str(int(sHolding * 100)/ 100.0) + '\n'
out += " Total Deduction: " + "$" + \
       str(int(deduction * 100)/100.0) + '\n'
out += "Net Pay: " + "$" + str(int(pay * 100)/100.0) + '\n'

#display result
print(out)
      

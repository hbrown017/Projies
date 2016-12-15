'''
Assignement: Car Loan Payment
Name: Harry Brown III
Date: 6/27/16
'''
from tkinter import *

class loanPayment:
    def __init__(self):

        # Create the main window.
        window = Tk()
        window.title("Car Loan")
        
        #amount of loan
        self.lblPrincipal = Label(window, text='Amount of loan: ') #label
        self.lblPrincipal.grid(row=0, pady=7, sticky=E)
        self.eloan = Entry(window, width=10) #entry
        self.eloan.grid(row=0, column=1, sticky=W)

        #interest rate
        self.lblInterestRate = Label(window, text='Interest rate (as %): ') #label
        self.lblInterestRate.grid(row=1, pady=7, sticky=E)
        self.erate = Entry(window, width=5) #entry
        self.erate.grid(row=1, column=1, sticky=W)

        #number of years
        self.lblNumberOfYears = Label(window, text='Number of years: ') #label
        self.lblNumberOfYears.grid(row=3, pady=7, sticky=E)
        self.eyears = Entry(window, width=2) #entry
        self.eyears.grid(row=3, column=1, sticky=W)

        #create string variable for monthly payment
        self.calValue = StringVar()

        #calculate payment
        self.btnCalculate = Button(window, text='Calculate Monthly Payment', command=self.calculate)
        self.btnCalculate.grid(row=4, columnspan=2, padx=70, pady=7)

        self.lblMonthlyPayment = Label(window, text='Monthly payment: ')
        self.lblMonthlyPayment.grid(row=5, pady=7, sticky=E)

        self.ecalValue = Entry(window, textvariable=self.calValue, state='readonly', width=10)
        self.ecalValue.grid(row=5, column=1, sticky=W)

        #Get all the values and use button to calculate the payment and display.
        window.mainloop()

    def calculate(self):
       p = eval(self.eloan.get())
       r = eval(self.erate.get())
       n = eval(self.eyears.get())*12
       I = r/1200
       payment = (p * I) / (1 - (1 + I) ** -n)
       self.calValue.set('$' + str(format(payment, '.2f'))) #set value for label

# Create an instance of loanpayment class.
mpay = loanPayment()

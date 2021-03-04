#!/usr/bin/env python3

# INTEREST CALCULATOR by Polymechanos and released under GPLv3

import math

mode = str.upper(input("""\

===================
INTEREST CALCULATOR 
===================

* To calculate final (A)mount, type 'A'.
* To calculate (T)ime to mature to a given balance, type 'T'.
* To calculate how much should be invested to achieve a given balance, type 'I'.

* Type 'help' for a detailed explanation of how to use this program.

* To (Q)uit, type 'Q'.
> \
"""))

on = True

while on == True:
    if mode == "A":
        principle = float(input("\nEnter Principle here: "))
        n = int(input("Number of compoundings per year: "))
        u = float(input("Average investment per compounding period: "))
        rate = float(input("Enter interest rate %: ")) 
        r = rate/100     #Converts interest to percentage
        t = float(input("Number of years to compute: "))
        Amount = principle * (1 + (u/principle) + (r/n))**(n*t)     #Compound interest formula.
        final = round(Amount, 8)
        print(f"\nIn {t} years, {principle} will have grown to {final}.\n")
        mode = str.upper(input(" Please select (A)mount, (T)ime, (I)nvestment, or (Q)uit.\n > "))
    elif mode == "T":
        principle = float(input("\nEnter Principle here: "))
        n = int(input("Number of compoundings per year: "))
        u = float(input("Average investment per compounding period:"))
        rate = float(input("Enter interest rate %: "))
        r = rate/100     #Converts interest to percentage
        a = float(input("Enter final value of investment: "))
        T1 = math.log(a/principle)    
        T2 = n*math.log(1+(u/principle)+r/n)
        Time = T1/T2    #Interest formula solved for time.
        final = round(Time, 2)
        print(f"\n{principle} will grow to {a} in {final} years.\n")
        mode = str.upper(input(" Please select (A)mount, (T)ime, (I)nvestment or (Q)uit.\n > "))
    elif mode == "I":
        principle = float(input("\nEnter Principle here: "))
        n = int(input("Number of compoundings per year: "))
        rate = float(input("Enter interest rate %: ")) 
        r = rate/100     #Converts interest to percentage
        t = float(input("Number of years to compute: "))
        a = float(input("Enter final value of investment: "))
        i1 = principle        #This stuff just breaks the compound interest formula into bits to make the formula easier to manage. We're solving for 'u' here.
        i2 = 1/(n*t) 
        i3 = (a/principle)**i2
        i4 = -1-(r/n)
        investment =  i1 * (i3 + i4)
        final = round(investment, 8)
        print(f"\n To grow {principle} to {a} in {t} years, you will need to invest {final} per compounding period.\n")
        mode = str.upper(input(" Please select (A)mount, (T)ime, (I)nvestment, or (Q)uit.\n > "))
    elif mode == "H" or mode == "HELP":
        print("""
---- HELP ----
              
** Mode Options ** 
              
    (A) AMOUNT
        Calculates the final amount of an investment over a given amount of time.

    (T) TIME
        Calculates the amount of time an investment will take to reach a certain balance.
        
    (I) INVESTMENT
        Calculates the amount you must invest each compounding period to reach a given balance in a given amount of time.

    NOTE: Modes A and T provide the option to include periodic deposits on top of the principle. (Ex. You deposit $100 into an investment account every month). Note, however, that for proper calculation the deposit frequency must match the compounding frequency (i.e. if the interest is compounded monthly, the deposit required is also monthly). 
    
    
** Input fields **
              
    PRINCIPLE -- initial investment amount / initial balance

    NUMBER OF COMPOUNDINGS PER YEAR -- number of times interest is added to the principle
         ~ Common values are 1 (simple interest), 12 (once per month), 365 (once per day).

    INVESTMENT PER COMPOUNDING PERIOD -- how much additional money you are contributing to the balance
         ~ Example: If the interest is compounded monthly, you would enter the average amount you add to the balance per month.
              
    INTEREST RATE -- the calculator converts your entry to a decimal automatically, so, for 6% interest, enter "6".

    NUMBER OF YEARS TO COMPUTE -- to calculate in months rather than years, use a decimal approximation 
         ~ Example: to calculate the interest over six months, use 0.5. To calculate the interest over one month, enter 0.0833.


              """)
        mode = str.upper(input(" Please select (A)mount, (T)ime, (I)nvestment, or (Q)uit.\n > "))
    elif mode == "Q" or mode == "QUIT" or mode == "STOP":
        on = False
        print("\n ***Invest wisely; give generously.*** \n")
    else:
        mode = str.upper(input("""
Please try again. Do you want to calculate (A)mount, (T)ime, (I)nvestment, or (Q)uit?
For help, type 'help'.
> \
""")) 

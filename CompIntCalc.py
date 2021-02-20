#!/usr/bin/env python3

import math

mode = str.upper(input("""\
INTEREST CALCULATOR
===================
* To calculate final (A)mount, type 'A'.
* To calculate (T)ime to mature to a given balance, type 'T'.
* To calculate how much should be (I)nvested to achieve a given balance, type 'I'.
* To (Q)uit, type 'Q'.
> \
"""))

on = True

while on == True:
    if mode == "A":
        principle = float(input("\nEnter Principle here: "))
        u = float(input("Average monthly investment: "))
        n = int(input("Number of compoundings per year: "))
        rate = float(input("Enter interest rate %: ")) 
        r = rate/100     #Converts interest to percentage
        t = int(input("Number of years to compute: "))
        Amount = principle * (1 + (u/principle) + (r/n))**(n*t)     #Compound interest formula.
        final = round(Amount, 2)
        print(f"\nIn {t} years, {principle} will have grown to {final}.\n")
        mode = str.upper(input(" Please select (A)mount, (T)ime, (I)nvestment, or (Q)uit.\n >"))
    elif mode == "T":
        principle = float(input("\nEnter Principle here: "))
        u = float(input("Average monthly investment: "))
        n = int(input("Number of compoundings per year: "))
        rate = float(input("Enter interest rate %: "))
        r = rate/100     #Converts interest to percentage
        a = float(input("Enter final value of investment: "))
        T1 = math.log(a/principle)    
        T2 = n*math.log(1+(u/principle)+r/n)
        Time = T1/T2    #Interest formula solved for time.
        final = round(Time, 2)
        print(f"\n{principle} will grow to {a} in {final} years.\n")
        mode = str.upper(input(" Please select (A)mount, (T)ime, (I)nvestment or (Q)uit.\n >"))
    elif mode == "I":
        principle = float(input("\nEnter Principle here: "))
        n = int(input("Number of compoundings per year: "))
        rate = float(input("Enter interest rate %: ")) 
        r = rate/100     #Converts interest to percentage
        t = int(input("Number of years to compute: "))
        a = float(input("Enter final value of investment: "))
        #Amount = principle * (1 + (u/principle) + (r/n))**(n*t)     #Compound interest formula.
        i1 = principle
        i2 = 1/(n*t)
        i3 = (a/principle)**i2
        i4 = -1-(r/n)
        investment =  i1 * (i3 + i4)
        final = round(investment, 2)
        print(f"\n To grow {principle} to {a} in {t} years, you will need to invest {final} per compounding period.\n")
        mode = str.upper(input(" Please select (A)mount, (T)ime, (I)nvestment, or (Q)uit.\n >"))
    elif mode == "Q":
        on = False
        print("Goodbye.")
    else:
        mode = str.upper(input("Please try again. Do you want to calculate (A)mount or (T)ime?"))



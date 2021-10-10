# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 15:37:26 2021

@author: Vik210
"""

#imports
import os

#declaring variables for the math operations and data

monthsTotal=[]
changes=[]
gains=[]

#path to get the csv data

csvpath=os.path.join('Resources','budget_data.csv')

# CSV reader specifies delimiter and variable that holds contents

with open(csvpath, 'r') as fileReader:
    row = fileReader.read()

    row = row.split("\n")
    
    for i in range(1,len(row)-1) :
        
        index = row[i].split(',')
        
        gains.append(int(index [1]))
        
        monthsTotal.append(index[0])
        
        
        #Print results for total months 

    print("Financial Analysis")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    
    print("Total Months: " + str(len(monthsTotal)))
    print("Total: $" + str(sum(gains)))

    for i in range(1,len(gains)):
        changes.append(gains[i]-gains[i-1])
    meanAverage=sum(changes)/len(changes)
    
    greatesIncrease=max(changes)
    greatestDecrease=min(changes)

    print("Average Change : $"+str(round(meanAverage,2)))

    print("Greatest increase in profits:  " + monthsTotal[changes.index(greatesIncrease)+1] + "  " + "$" + str(greatesIncrease))

    print("Greatest Decrease in profits: " + monthsTotal[changes.index( greatestDecrease) + 1] + "  " + "$" + str( greatestDecrease))


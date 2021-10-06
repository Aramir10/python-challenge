# This will allow us to create file paths across operating systems &  Module for reading CSV files
import os
import csv

#lists and variables for candidates, data & total

candidates=[]
grandTotal=[]
percetTotal=[]
total=0

#dictionary to store the name of the candidate & votes
data ={}

#path for election data csv
csvpath = os.path.join( 'Resources', 'election_data.csv')

#verifypath
#print(csvpath)

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

   # print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        print(row)

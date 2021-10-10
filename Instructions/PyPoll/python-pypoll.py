# This will allow us to create file paths across operating systems &  Module for reading CSV files
import os
import csv

#lists and variables for candidates, data & total

candidateKhan=0
candidateCorrey=0
candidateLi=0
candidateOT=0
grandTotal=0
voteTotalMax=0

#dictionary to store the name of the candidate & votes
#data ={}

# Function to get the percentage of votes for each candiate percetTotal

def percetTotal (candidatePer, voterCount ):
    return(100 * float(candidatePer)/float(voterCount))


#path for election data csv
csvpath = os.path.join( 'Resources', 'election_data.csv')

#verifypath
#print(csvpath)

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

   # print(csvreader)

    # Read the header row first (skip this step if there is now header)
   # csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    #for row in csvreader:
     #   print(row)
     
     
    for votes in csvreader:
        
        contestant = votes[2]
        
        grandTotal = grandTotal + 1
        
        if contestant == "Khan":
            
            candidateKhan = candidateKhan + 1
        
        if contestant == "Correy":
           
            candidateCorrey = candidateCorrey + 1
       
        if contestant == "Li":
           
            candidateLi = candidateLi + 1
        
        if contestant == "O'Tooley":
           
            candidateOT = candidateOT + 1
            
        candidateData = {"Khan": candidateKhan, "Correy": candidateCorrey, "Li": candidateLi, "O'Tooley": candidateOT}
        
       
        
       #findout who is  the election winner 
       
        for contestant, score in candidateData.items():
            
            if score > voteTotalMax:
               
                voteTotalMax = score
               
                ElectionWinner = contestant
                
                
                #print statements with results

print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')  
print(' ')              
print('ELECTION RESULTS   ')
print(' ')
print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-'+'\n')
print(f'Total Votes: {grandTotal}'+'\n')

print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')

print(f'Candidate Khan: {percetTotal(candidateKhan,grandTotal):.3f}%  ({candidateKhan})')
print(' ')
print(f'Candidate Correy: {percetTotal(candidateCorrey,grandTotal):.3f}%  ({candidateCorrey})')
print(' ')
print(f'Candidate Li: {percetTotal(candidateLi,grandTotal):.3f}%  ({candidateLi})')
print(' ')
print(f'Candidate OTooley: {percetTotal(candidateOT,grandTotal):.3f}%  ({candidateOT})')
print(' ')
print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')
print(f'The Election Winner is {ElectionWinner} !!!! ')
print('-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-')

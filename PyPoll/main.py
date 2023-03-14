
#import modules
import os
import csv

#set path
pypollcsv = os.path.join("Resources","Election_data.csv")

#lists to store data
Totalvotes = 0
VotesPerCandidate = {}
candidate = []
CandidateL = []



#open csv
with open(pypollcsv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
#Read each row    
    for row in csvreader:
        Totalvotes += 1
        if row[2] not in VotesPerCandidate:
            VotesPerCandidate[row[2]] = 1
        else:
            VotesPerCandidate[row[2]] += 1


ScandidateL = sorted(CandidateL)

print("Election Results")
print("-"*75)
print("Total Votes: " + str(Totalvotes))
print("-"*75)
#stuck here
print("-"*75)
winner = max(VotesPerCandidate, key=VotesPerCandidate.get)
print(f"Winner: {winner}")


with open('electionresults.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("-"*75 + "\n")
    text.write("Total Votes: " + str(Totalvotes) + "\n")
    text.write("-"*75 + "\n")
    text.write("-"*75 + "\n")
    text.write(f"Winner: {winner}")
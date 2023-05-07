#import modules
import csv
import os

#Path and outpath
pollcsv = os.path.join('Resources','election_data.csv')
outpath = "Analysis\output.txt"

#Declare lists
vote_list = []
winner_list = []

print("Election Results")
print("---------------------------------")

#open csv file
with open(pollcsv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

#find the total number of rows
    rowcount = 0
   
    for row in csvreader:   
        rowcount = rowcount + 1 
    print("Total Votes: " + str(rowcount))
    print("---------------------------------")

#Candidate List
with open(pollcsv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    candidate_list = {}
    
    for row in csvreader:  
        candidate = str(row[2])
        if candidate not in candidate_list:
            candidate_list[candidate] = 1
        else:
            candidate_list[candidate] += 1
        

# calculate percentage
    for candidates in candidate_list:
        percentage = ((candidate_list[candidates])/rowcount)*100
        print(f"{candidates}: {percentage:.3f}% ({candidate_list[candidates]})")
        vote_list.append(candidate_list[candidates])
        winner_list.append(candidates)
    print("---------------------------------")
    
    #find the winner
    max_vote = max(vote_list)
    winner_index = vote_list.index(max_vote)
    print(f"Winner: {winner_list[winner_index]}")
    print("---------------------------------")

#export to a text file
with open(outpath, 'w') as txtfile:
    txtfile.write(f"Election Results\n")
    txtfile.write(f"----------------------------\n")
    txtfile.write(f"Total Votes: {rowcount}\n")   
    txtfile.write(f"----------------------------\n")
    for c in candidate_list:
        percentage = ((candidate_list[candidates])/rowcount)*100
        txtfile.write(f"{candidates}: {percentage:.3f}% ({candidate_list[candidates]})\n")
    txtfile.write(f"----------------------------\n")
    txtfile.write(f"Winner: {winner_list[winner_index]}\n") 
    txtfile.write(f"----------------------------\n")
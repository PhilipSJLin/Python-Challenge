#import modules
import csv
import os

#Path and outpath
bankcsv = os.path.join('Resources','budget_data.csv')
outpath = "Analysis\output.txt"

#Declare lists and values
date = [0]
profit = [1]
total_profit_loss = 0
total_change = 0
change = 0
change_list = []
month_list = []

print("Financial Analysis")
print("-------------------------------")

#Total Months
with open(bankcsv, 'r') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    rowcount = 0

    for row in csvreader:
        rowcount = rowcount + 1 
    print("Total Months: " + str(rowcount))

#Total Profit-Loss
with open(bankcsv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader: 
        total_profit_loss = total_profit_loss + int(row[1])
    print("Total: " + "$" + str(total_profit_loss))

#Change and Average Change
with open(bankcsv, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    first_row = next(csvreader)
    previous = int(first_row[1])
    for row in csvreader:     
        change = int(row[1]) - previous
        change_list.append(change)
        month_list.append(row[0])
        total_change = total_change + change

        avg_change = total_change / (rowcount - 1)
        previous = int(row[1])
    print(f"Average Change: ${avg_change:.2f}")
   
    # Greatest Increase in Profits
    max_change = max(change_list)
    max_index = change_list.index(max_change)
    print(f"Greatest Increase in Profits: {month_list[max_index]} (${max_change})")

    #Greatest Decrease in Profits
    min_change = min(change_list)
    min_index = change_list.index(min_change)
    print(f"Greatest Decrease in Profits: {month_list[min_index]} (${min_change})")
    

#export to a text file
with open(outpath, 'w') as txtfile:
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"----------------------------\n")
    txtfile.write(f"Total Months: {rowcount}\n")   
    txtfile.write(f"Total: ${total_profit_loss}\n")
    txtfile.write(f"Average Change: ${avg_change:.2f}\n") 
    txtfile.write(f"Greatest Increase in Profits: {month_list[max_index]} (${max_change})\n")   
    txtfile.write(f"Greatest Decrease in Profits: {month_list[min_index]} (${min_change})") 
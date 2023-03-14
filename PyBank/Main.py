#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period

#import modules
import os
import csv

#set path
budget_csv = os.path.join("Resources", "budget_data.csv")

#lists to store data
monthsT = 0
profitloss = []
Total = 0
MonthlyChanges = []
months = []

#read csv file
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # skip first row which contains headers
    csvheader = next(csvreader)

    #read through each row
    for row in csvreader:
        monthsT += 1
        Total += int(row[1])
        profitloss.append(row[1])
        months.append(row[0])

#base profit loss value
PLbase = int(profitloss[0])

#monthly changes
for i in range(1, len(profitloss)):
    MonthlyChanges.append(int(profitloss[i]) - PLbase)
    PLbase = int(profitloss[i])
    i += 1

MaxIncrease = max(MonthlyChanges)
MaxDecrease = min(MonthlyChanges)

#calculate Average Change



#month index
for i in range(len(MonthlyChanges)):
    if MonthlyChanges[i] == MaxIncrease:
        maxIndex = (i - 1)
    elif MonthlyChanges[i] == MaxDecrease:
        minIndex = (i - 1)
    else:
        i += 1
        
MaxMonth = months[maxIndex]
MinMonth = months[minIndex]

#print financial analysis
print("Financial Analysis")
print("-"*75)
print(f"Total Months: {monthsT}")
print(f"Total: ${Total}")
print(f"Average Change = $ ")
print(f"Greatest Increase in Profits: {MaxMonth} (${MaxIncrease})")
print(f"Greatest Decrease in Profits: {MinMonth} (${MaxDecrease})")
print("-"*75)

#export a text file with results
with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(monthsT) + "\n")
    text.write("    Total: " + "$" + str(Total) +   "\n")
    text.write("    Greatest Increase in Profits: " + str(MaxMonth) + "($" + str(MaxIncrease) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(MinMonth) + "($" + str(MaxDecrease) + ")\n")
    text.write("----------------------------------------------------------\n")
import os
import csv

#Define Path
pybank = os.path.join('..', 'Resources', 'budget_data.csv')
with open('budget_data.csv','r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)

    #Set Empty Lists for Variables
    months_total = []
    profit_total = []
    profit_change = []
               
    #Loop through Data
    for row in csvreader:
        months_total.append(row[0])
        profit_total.append(int(row[1]))
    for i in range(len(profit_total)-1):
        profit_change.append(profit_total[i+1]-profit_total[i])
                      
#Find Increases and Decreases in Profit
increase = max(profit_change)
decrease = min(profit_change)

month_increase = profit_change.index(max(profit_change))+1
month_decrease = profit_change.index(min(profit_change))+1

#Print Results
print("Financial Analysis")
print("------------------------")
print(f"Total Months: {len(months_total)}")
print(f"Total: ${sum(profit_total)}")
print(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {months_total[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {months_total[month_decrease]} (${(str(decrease))})")      

#Create text File (Financial Analysis)
output = os.path.join('..', 'Analysis', 'Financial_Analysis.txt')
with open(output, 'w') as text_file:
    text_file.write("Financial Analysis")
    text_file.write("\n")
    text_file.write("------------------------")
    text_file.write("\n")
    text_file.write(f"Total Months: {len(months_total)}")
    text_file.write("\n")
    text_file.write(f"Total: ${sum(profit_total)}")
    text_file.write("\n")
    text_file.write(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
    text_file.write("\n")
    text_file.write(f"Greatest Increase in Profits: {months_total[month_increase]} (${(str(increase))})")
    text_file.write("\n")
    text_file.write(f"Greatest Decrease in Profits: {months_total[month_decrease]} (${(str(decrease))})")
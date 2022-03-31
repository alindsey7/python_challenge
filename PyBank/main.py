import csv
import sys
import os
file = open('Resources/budget_data.csv')
csvreader = csv.reader(file)

header = []
header = next(csvreader)

rows = []
months = 0
Profit = 0
maxProfit = -sys.maxsize - 1
minProfit = sys.maxsize
maxProfitStr = ''
minProfitStr = ''
for row in csvreader:
    rows.append(row)
    monthlyEarnings = int(rows[months][1])
    if(months!= 0):
        prevMonthEarnings = int(rows[months-1][1])
        if monthlyEarnings - prevMonthEarnings > maxProfit:
            maxProfit = monthlyEarnings - prevMonthEarnings
            maxProfitStr = rows[months][0]
        if monthlyEarnings - prevMonthEarnings < minProfit:
            minProfit = monthlyEarnings - prevMonthEarnings
            minProfitStr = rows[months][0]
    Profit += monthlyEarnings
    months += 1
avgChange = (int(rows[months-1][1]) - int(rows[0][1]))/(months-1)
avgChange = round(avgChange,2)
file.close()
outputPath = os.path.join('Analysis','analysis.txt')
with open(outputPath, 'w') as f:
    f.write(f'Financial Analysis \n----------------------------------\nTotal Months: {months} \nTotal: {Profit} \nAverage Change {avgChange} \nGreatest Increase in Profits {maxProfitStr} (${maxProfit}) \nGreatest Decrease in Profits: {minProfitStr} (${minProfit})')
print("Financial Analysis")
print("----------------------------------")
print(f'Total Months: {months} \nTotal: {Profit} \nAverage Change {avgChange} \nGreatest Increase in Profits {maxProfitStr} (${maxProfit}) \nGreatest Decrease in Profits: {minProfitStr} (${minProfit})')
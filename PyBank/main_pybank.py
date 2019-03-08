import csv
import os

pybank_csv = os.path.join('03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv')


#open csv file and count total lines
with open(pybank_csv, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	csv_header = next(csvfile)
	
	line_count = sum(1 for line in csvreader)
	
print(f'Total Months: {line_count}')


#open csv file and add all Profits/Losses
with open(pybank_csv, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	csv_header = next(csvfile)
	
	total = 0
	for line in csvreader:
		total += int(line[1])

print(f'Total: ${total}')


#open csv file and find average daily change
with open(pybank_csv, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	csv_header = next(csvfile)

	dailyChangeList = []

	prev = 0
	for line in csvreader:
		
		thismonth = int(line[1])
		dif = thismonth - prev
		prev = thismonth
		dailyChangeList.append(dif)

dailyChangeList.pop(0) #pop off first value since changes start after first month

average = round(sum(dailyChangeList)/len(dailyChangeList),2)
print(f'Average Change: ${average}')


#find greatest increase and decrease from daily changes
greatestIncrease = max(dailyChangeList)
greatestDecrease = min(dailyChangeList)

GrInMn_index = dailyChangeList.index(greatestIncrease)
GrDeMn_index = dailyChangeList.index(greatestDecrease)


with open(pybank_csv, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	csv_header = next(csvfile)

	months = []
	for line in csvreader:
		months.append(line[0])
		
greatestIncreaseMonth = (months[GrInMn_index + 1]) #add 1 because popped first number
greatestDecreaseMonth = (months[GrDeMn_index + 1]) #add 1 because popped first number

print(f'Greatest Increase in Profits: {greatestIncreaseMonth} ${greatestIncrease}')
print(f'Greatest Decrease in Profits: {greatestDecreaseMonth} ${greatestDecrease}')


#code should work with varying data in same format!

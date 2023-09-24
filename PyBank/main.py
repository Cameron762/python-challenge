import csv

csvpath = '/Users/cameron-wadecarson/Desktop/bootcamp/python-challenge/PyBank/Resources/budget_data.csv'
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    dates = []
    net = []
    # appending rows in csv to lists
    for row in csvreader:
        dates.append(row[0])
        net.append(int(row[1]))

    # calling on lists to calculate everything
    months = len(dates)
    nettotal = sum(net)
    avprof = round(nettotal / months)
    highest = max(net)
    lowest = min(net)

    # using .index to ge the actual month out of csv
    highestindex= net.index(highest)
    lowestindex = net.index(lowest)
    bestmonth = dates[highestindex]
    worstmonth = dates[lowestindex]

print('Financial Analysis')
print('-----------------------')
print(f'Total Months: {months}')
print(f'Total: ${nettotal}')
print(f'Average Change: ${avprof}')
print(f'Greatest Increase in Profits: {bestmonth} ${highest}')
print(f'Greatest Decrease in Losses: {worstmonth} ${lowest}')

resultspath = '/Users/cameron-wadecarson/Desktop/bootcamp/python-challenge/PyBank/Results/results.txt'
with open(resultspath, "w") as txtfile:
    txtfile.write('Financial Analysis\n')
    txtfile.write('-----------------------\n')
    txtfile.write(f'Total Months: {months}\n')
    txtfile.write(f'Total: ${nettotal}\n')
    txtfile.write(f'Average Change: ${avprof}\n')
    txtfile.write(f'Greatest Increase in Profits: {bestmonth} ${highest}\n')
    txtfile.write(f'Greatest Decrease in Losses: {worstmonth} ${lowest}\n')


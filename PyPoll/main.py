import csv
from collections import Counter

votes = []
candidates = []

csvpath = '/Users/cameron-wadecarson/Desktop/bootcamp/python-challenge/PyPoll/Resources/election_data.csv'
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvreader)

    #appending rows 0 and 2 into lists 
    for row in csvreader:
        votes.append(row[0])
        candidates.append(row[2])

    # counts length of votes list to get total vote count
    votecount = len(votes)
    # puts Counter function into var to be called in for loop w/ .items
    candidatecount = Counter(candidates)
    # puts .most_common into a callable var
    winner = candidatecount.most_common(1)[0]

    print('Election Results')
    print('-------------------')
    print(f'Total Votes: {votecount}')
    print('-------------------')
    # had to move entire loop so it would print all 3 candidate results
    for candidate, count in candidatecount.items():
        percentage = (count / votecount) * 100
        print(f'{candidate}: {percentage:.3f}% ({count})')
    print('-------------------')
    print(f'Winner: {winner[0]}')
    print('-------------------')

resultspath = '/Users/cameron-wadecarson/Desktop/bootcamp/python-challenge/PyPoll/Analysis/results.txt'
with open(resultspath, "w") as txtfile:
    txtfile.write('Election Results\n')
    txtfile.write('-------------------\n')
    txtfile.write(f'Total Votes: {votecount}\n')
    for candidate, count in candidatecount.items():
        percentage = (count / votecount) * 100
        txtfile.write(f'{candidate}: {percentage:.3f}% ({count})\n')
    txtfile.write('-------------------\n')
    txtfile.write(f'Winner: {winner[0]}\n')
    txtfile.write('-------------------\n')

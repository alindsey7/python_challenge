import csv
import sys
import os
file = open('Resources/election_data.csv')
csvreader = csv.reader(file)

header = []
header = next(csvreader)

rows = []
votes = 0
candidates = []
candidateVotes = []
for row in csvreader:
    rows.append(row)
    index = 0
    flag = True
    for index in range(len(candidates)):
        if(candidates[index] == rows[votes][2]):
            candidateVotes[index] += 1
            flag = False
    if(flag):
        candidates.append(rows[votes][2])
        candidateVotes.append(1)
    votes += 1
print(f'Election Results \n--------------------------\nTotal Votes: {votes}\n--------------------------\n')
percentage = []
winningVotes = -1
winner = ''
for i in range(len(candidates)):
    percentage.append(round(candidateVotes[i]/votes * 100,3))
    print(f'{candidates[i]}: {percentage[i]}% ({candidateVotes[i]})')
    if(winningVotes < candidateVotes[i]):
        winningVotes = candidateVotes[i]
        winner = candidates[i]
print("--------------------------")
print(f'Winner: {winner}')
outputPath = os.path.join('Analysis','analysis.txt')
with open(outputPath, 'w') as f:
    f.write(f'Election Results \n--------------------------\nTotal Votes: {votes}\n--------------------------\n')
    for i in range(len(candidates)):
        f.write(f'{candidates[i]}: {percentage[i]}% ({candidateVotes[i]})\n')
    f.write(f'--------------------------\nWinner: {winner}')
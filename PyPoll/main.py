import os
import csv
from collections import Counter


infile = os.path.join("C:\\Users\\tsegi\\OneDrive\\Desktop\\Python_challenge_resubmission-1\\PyPoll\\Resources\\election_data.csv")
outfile = os.path.join("C:\\Users\\tsegi\\OneDrive\\Desktop\\Python_challenge_resubmission-1\\PyPoll\\Resources\\election_analysis.txt")

count = 0
candidate_list = []
unique_candidate = []
vote_count = []
vote_percent = []


with open(infile, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    for row in csvreader:
    # total number of votes
        count = count + 1

    # Candidates name
        candidate_list.append(row[2])

    # 'a' as unique candidate names
    for a in set(candidate_list):
        unique_candidate.append(a)

    # 'b' as number of votes per candidate
        b = candidate_list.count(a)
        vote_count.append(b)

    # 'c' as percent of total votes per candidate
        c = (b/count)*100
        vote_percent.append(c)
        
    winning_vote_count = max(vote_count)
    winner = unique_candidate[vote_count.index(winning_vote_count)]
    
print("-------------------------")
print("Election Results")   
print("-------------------------")
print("Total Votes :" + str(count))    
print("-------------------------")
for i in range(len(unique_candidate)):
            print(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i])+ ")\n")
print("-------------------------")
print("The winner is: " + winner)
print("-------------------------")

# Print to a text file: election_results.txt

f = open(outfile, "w")
f.write("Election Results")
f.write('\n')
f.write("-------------------------")
f.write('\n')
f.write("Total Votes: " + str(count))
f.write('\n')
f.write("-------------------------")
f.write('\n')
for i in range(len(set(unique_candidate))):
    f.write(unique_candidate[i] + ": " + str(vote_percent[i]) +"% (" + str(vote_count[i]) + ")  \n")
f.write('\n')
  
f.write("-------------------------") 
f.write('\n')
f.write(f"Winner: {winner}")
f.write('\n')

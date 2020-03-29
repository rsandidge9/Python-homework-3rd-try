#•	Your task is to create a Python script that analyzes the records to calculate each of the following:
# This will allow us to create file paths across operating systems
# Module for reading CSV files
import os
import csv

#Path to collect data from here folder
pollcsv = os.path.join('Resources','election_data.csv')

#create lists from dataset
candidate_unique = []
cadidate_vote_total = []
percent_vote = []

#create variable
total = 0

#open csv file
with open(pollcsv, newline='') as csvfile:

#read csv file
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
# The total number of votes cast
    for row in csvreader:
        #+= means addition assignment assigns the result to the varible total
        total += 1
    
    #create candidate list and add names to the list
        #####candidate_list.append(row[2])
        candidate_in_file = (row[2])    
#	A complete list of candidates who received votes
    #https://docs.python.org/3/tutorial/datastructures.html#tut-listcomps
        candidate_in_file = (row[2])
        if candidate_in_file in candidate_unique:
            candidate_index = candidate_unique.index(candidate_in_file)
            candidate_vote_total[candidate_index] = candidate_vote_total[candidate_index] + 1
        else:
            candidate_unique.append(candidate_in_file)
            candidate_vote_total.append(1)    
#	The percentage of votes each candidate won
    percentage = []
    max_votes = candidate_vote_total[0]
    max_index = 0
    for x in range(len(candidate_unique)):
        #round to two decimals using round
        vote_percentage = round(candidate_vote_total[x]/total*100, 2)
        percentage.append(vote_percentage)

        if candidate_vote_total[x] > max_votes:
            max_votes = candidate_vote_total[x]
            max_index = x
    election_winner = candidate_unique[max_index]
    
    
#	The total number of votes each candidate won


#	The winner of the election based on popular vote.
print("--------------------------------------------")
print("election results")
print("--------------------------------------------")
#print("Total Votes" + str(total))
print(f'Total Votes {total}')
for x in range(len(candidate_unique)):
    print(f'{candidate_unique[x]} {percentage[x]} ({candidate_vote_total[x]})')
print(f'Election Winner = {election_winner}')

with open("election results.txt", "w") as text:
    text.write("--------------------------------------\n")
    text.write("election results\n")
    text.write("-------------------------------------\n\n")
    text.write(f'Total Votes {total}')
    for x in range(len(candidate_unique)):
        text.write(f'{candidate_unique[x]} {percentage[x]} ({candidate_vote_total[x]})')
    text.write(f'Election Winner = {election_winner.upper()}')
text.write("END")
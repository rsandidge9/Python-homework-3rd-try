#•	Your task is to create a Python script that analyzes the records to calculate each of the following:
# This will allow us to create file paths across operating systems
# Module for reading CSV files
import os
import csv

#Path to collect data from here folder
pollcsv = os.path.join('Resources','election_data.csv')

#create lists from dataset
candidate_list = []
candidate_name = []
vote_total = []
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
        total_votes = total + 1
    
    #create candidate list and add names to the list
        #####candidate_list.append(row[2])
        candidate_in = (row[2])    
#	A complete list of candidates who received votes
    #https://docs.python.org/3/tutorial/datastructures.html#tut-listcomps
        candidate_in = (row[2])
        if candidate_in in candidate_list:
            candidate_index = candidate_list.index(candidate_in)
            vote_total[candidate_index] = vote_total[candidate_index] + 1
        else:
            candidate_list.append(candidate_in)
            vote_total.append(1)    
#	The percentage of votes each candidate won
    percentage = []
    max_votes = vote_total[0]
    max_index = 0
    for x in range(len(candidate_name)):
        vote_percentage = round(vote_total[x]/total_votes*100, 2)
        percentage.append(vote_percentage)

        if vote_total[x] > max_votes:
            max_votes = vote_total[x]
            max_index = x
    election_winner = candidate_list[max_index]
    
#	The total number of votes each candidate won


#	The winner of the election based on popular vote.


    for x in range(len(candidate_list)):
        print(f'{candidate_in[x]} : {percentage[x]}% ({vote_total[x]})')
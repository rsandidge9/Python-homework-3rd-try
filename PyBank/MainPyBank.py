#•	Your task is to create a Python script that analyzes the records to calculate each of the following:
# This will allow us to create file paths across operating systems
# Module for reading CSV files
import os
import csv

#Path to collect data from here folder
profitcsv = os.path.join('Resources', 'budget_data.csv')

#Create variables
months = 0
total = 0

#Create lists
net_change = []
month_change = []

#Create dictionary
greatest_increase = {"date":"", "change": 0}
greatest_decrease = {"date":"", "change": 999999999}

#open CSV file
with open(profitcsv, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)
    first_row = next(csvreader)
    total = total + int(first_row[1])
    pre_row = int(first_row[1])
    months = months + 1


    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        months = months + 1
        p_l = int(row[1])
        total = total + p_l
        change = p_l - pre_row
        pre_row = p_l 
        net_change.append(change)
        month_change.append(row[0])

        if change > greatest_increase ["change"]:
            greatest_increase["date"]=row[0]
            greatest_increase["change"]=change

        if change < greatest_decrease ["change"]:
            greatest_decrease["date"]=row[0]
            greatest_decrease["change"]=change   
    print("--------------------------------------------")
    print("Analysis")
    print("--------------------------------------------")
    print("Total Months" + str(months))
    print("Total Profits" "$" +str(total))
    print("Average Change" + "$" + str(change))
    print("Greatest Change in profit" + "$" + str(greatest_increase))
    print("Greatest Decrease in profit" + "$" + str(greatest_decrease))
    print("--------------------------------------------")
with open("Analysis.txt", "w") as text:
    text.write("--------------------------------------\n")
    text.write("analysis" +"\n")
    text.write("-------------------------------------\n\n")
    text.write("Total Months: " +str(months) + "\n")
    text.write("Total Profits: " + "$" + str(total)+ "\n")
    text.write("Average Change: " + "$" + str(change)+ "\n")
    text.write("Greatest Change in Profit: " + "$" + str(greatest_increase)+ "\n")
    text.write("Greatest Decrease in Profit: " + "$" + str(greatest_decrease)+ "\n")   
    text.write("--------------------------------------\n")

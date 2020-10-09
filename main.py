# Import the dependencies 
import os
import csv

# Declare variables to store date, profit/losses and change in the profit/losses as lists
date = []
profit_losses = []
change = []

#Open and read csv file
with open("Resources/budget_data.csv", 'r') as csv_file:
    #Split data on commas
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Skip the header in the csv file
    header = next(csv_reader)

    # Skip the first row of data in the csv file 
    firstRow = next(csv_reader)
    Total_amount = int(firstRow[1])
    Month = 1
    Previous_pl = int(firstRow[1])
    greatest_increase = ["", 0]
    greatest_decrease = ["", 99999999999]

# Define a for loop and have it take 'budget_data' as its iterator
    for budget_data in csv_reader:
        Amount = int(budget_data[1])
        profit_losses.append(Amount)
        Total_amount += int(budget_data[1])
        change_pl = int(budget_data[1]) -Previous_pl
        change.append(change_pl)
        Previous_pl = int(budget_data[1])
        Month += 1

        # Total number of months can be found by adding all the rows in the date column together
        Total_months = Month

        #Total Profit/Losses can be found by adding all the values in the Profit/Losses' column
        if change_pl > greatest_increase[1]:
            greatest_increase[0] = budget_data[0]
            greatest_increase[1] = change_pl

        if change_pl < greatest_decrease[1]:
            greatest_decrease[0] = budget_data[0]
            greatest_decrease[1] = change_pl


        #Average changes in Profit/Losses over the entire period can be calculated by dividing the total profit/losses by the total number of months
        #Greatest_inc_profit = max(change)
        #Greatest_dec_profit = min(change)
Total_profit_losses = sum(change)        
Average_change_pl = Total_profit_losses / len(change)
# Print out the stats on the terminal
print("Financial Analysis")
print("-------------------------------------------------------")
print(f"Total Months: {Total_months}")
print(f"Total Profit/Losses: ${Total_amount}")
print(f"Average Change in Profit/Losses: ${Average_change_pl}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]}) \n")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]}) \n")

#print(Total_months)

# Put the stats in the text file 

output_txt = (f"Financial Analysis \n"
    f"------------------------------------------------------- \n"
    f" Total Months: {Total_months} \n"
    f"Total Profit/Losses: {Total_amount} \n"
    f"Average Change in Profit/Losses: {Average_change_pl} \n"
    f" Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]}) \n"
    f" Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]}) \n")

# Set variable for output file
budget_output_file = os.path.join(".", "Analysis", "web_final.txt")

#Open and write to the output file
with open(budget_output_file, "w", newline="") as datafile:
    writer = datafile.write(output_txt)

    


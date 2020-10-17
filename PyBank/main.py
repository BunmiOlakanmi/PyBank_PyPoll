# Import the dependencies 
import os
import csv

# Declare variables to store profit/losses and change in the profit/losses as lists
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

    # Set the initial value of Total amount 
    Total_amount = int(firstRow[1])
    
    # Initialize Month = 1
    Month = 1

    # Set the initial value of previous value of the profits and losses 
    Previous_pl = int(firstRow[1])
    
    # Initialize greatest increase and greatest decrease
    greatest_increase = ["", 0]
    greatest_decrease = ["", 99999999999]

    # Define a for loop and have it take 'budget_data' as its iterator
    for budget_data in csv_reader:
        # Set the values for Amount as values in the list budget_data[1] 
        # and append to the profit and losses
        Amount = int(budget_data[1])
        profit_losses.append(Amount)

        # Update Total_amount
        Total_amount += int(budget_data[1])

        # change_pl holds the changes in the profits and losses
        change_pl = int(budget_data[1]) - Previous_pl
        change.append(change_pl)
        Previous_pl = int(budget_data[1])
        Month += 1

        # Set the Total_months as the value in Month
        Total_months = Month

       # Check for the greatest increase  
        if change_pl > greatest_increase[1]:
            # Retrieve the date 
            greatest_increase[0] = budget_data[0]

            # Retrieve the value of the greatest increase
            greatest_increase[1] = change_pl

        # Check for the greatest decrease
        if change_pl < greatest_decrease[1]:
            # Retrieve the date
            greatest_decrease[0] = budget_data[0]

            # Retrieve the value of the greatest decrease
            greatest_decrease[1] = change_pl

# Total profit and losses equal the sum of all changes
Total_profit_losses = sum(change)    

# Average changes in Profit/Losses over the entire period can be calculated by dividing 
# the total profit and losses by the number of changes
Average_change_pl = round(Total_profit_losses / len(change),2)

# Print out the stats on the terminal
print("Financial Analysis")
print("-------------------------------------------------------")
print(f"Total Months: {Total_months}")
print(f"Total: ${Total_amount}")
print(f"Average Change: ${Average_change_pl}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]}) \n")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]}) \n")

# Put the stats in a text file 
output_txt = (f"Financial Analysis \n"
    f"------------------------------------------------------- \n"
    f"Total Months: {Total_months} \n"
    f"Total: ${Total_amount} \n"
    f"Average Change: ${Average_change_pl} \n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]}) \n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]}) \n")

# Set variable for output file
budget_output_file = os.path.join(".", "Analysis", "PyBank_Analysis.txt")

#Open and write to the output file
with open(budget_output_file, "w", newline="") as datafile:
    writer = datafile.write(output_txt)
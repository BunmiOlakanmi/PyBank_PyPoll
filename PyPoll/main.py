# Import all dependencies
import csv
import os

# Declare variables to store stats
#Dim Total_votes As Long



# Open and read csv file
with open("Resources/election_data.csv", 'r') as csv_file:
    #Split data on commas
    csv_reader = csv.reader(csv_file, delimiter=",")
   
    # Skip the header in the csv file
    header = next(csv_reader)
    
    # Declare variables to store total votes and sum of individual candidate's votes
    
    Total_votes = 0
    Khan_votes = 0
    Correy_votes = 0
    Li_votes = 0
    OTooley_votes = 0
    Win =''
    #Dim Winner As String 
    # Calculate total votes, and sum of individual candidate's votes    
    for row in csv_reader:
        Total_votes+=1
        if row[2] =='Khan':
            Khan_votes += 1
        elif    row[2] == 'Correy':
            Correy_votes +=1
        elif row[2] == 'Li':
            Li_votes +=1
        else:
            OTooley_votes += 1
    
    '''
    print(Khan_votes)
    print(Correy_votes)
    print(Li_votes)
    print(OTooley_votes)
    print(Total_votes)
    '''
    # Calculate Percentage votes for each candidate
    Pt_Khan_votes = Khan_votes / Total_votes
    Pt_Correy_votes = Correy_votes / Total_votes
    Pt_Li_votes = Li_votes / Total_votes
    Pt_OTooley_votes = OTooley_votes / Total_votes
    Percent_Khan_votes = "{:.3%}".format(Pt_Khan_votes)
    Percent_Correy_votes = "{:.3%}".format(Pt_Correy_votes)
    Percent_Li_votes = "{:.3%}".format(Pt_Li_votes)
    Percent_OTooley_votes = "{:.3%}".format(Pt_OTooley_votes)
    #print(Percent_Khan_votes)

# Find the winner by comparing their votes
# Winner_votes = max(Khan_votes, Correy_votes, Li_votes, OTooley_votes)
if Khan_votes > Correy_votes and Khan_votes > Li_votes and Khan_votes > OTooley_votes:
    Win = 'Khan'
elif Correy_votes > Khan_votes and Correy_votes > Li_votes and Correy_votes>OTooley_votes:
    Win = 'Correy'
elif Li_votes > Khan_votes and Li_votes>Correy_votes and Li_votes>OTooley_votes:
     Win = 'Li'
elif OTooley_votes > Khan_votes and OTooley_votes > Li_votes and OTooley_votes > Correy_votes:
    Win ='OTooley'

# Print results on the terminal
print("Election Results")
print("---------------------------")
print(f"Total Votes: {Total_votes} \n")
print("---------------------------")
print(f"Khan: {Percent_Khan_votes} ({Khan_votes}) \n")
print(f"Correy: {Percent_Correy_votes} ({Correy_votes}) \n")
print(f"Li: {Percent_Li_votes} ({Li_votes}) \n ")
print(f"O'Tooley: {Percent_OTooley_votes} ({OTooley_votes}) \n")
print("---------------------------")
print(f"Winner: {Win}  \n")
print("---------------------------")

# Print results to a text file
output_txt = (f"Election Results \n"  
f"---------------------------\n"
f"Total Votes: {Total_votes} \n"
f"---------------------------\n"
f"Khan: {Percent_Khan_votes} ({Khan_votes}) \n"
f"Correy: {Percent_Correy_votes} ({Correy_votes}) \n"
f"Li: {Percent_Li_votes} ({Li_votes}) \n "
f"O'Tooley: {Percent_OTooley_votes} ({OTooley_votes}) \n"
f"---------------------------\n"
f"Winner: {Win}  \n"
f"---------------------------\n")

# Set variable for output file
election_output_file = os.path.join(".", "Analysis", "web_final.txt")

# Open and write to the output file
with open(election_output_file, "w", newline="") as datafile:
    writer = datafile.write(output_txt)

    



import os
import csv

#Define Path
PyPoll = os.path.join('..', 'Resources', 'election_data.csv')
with open('election_data.csv','r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)

    #Set Variables as Zero 
    total_votes = 0
    khan_votes = 0
    correy_votes = 0
    li_votes = 0
    otooley_votes = 0

    #Loop through Data
    for row in csvreader:
        total_votes += 1
        if (row[2] == "Khan"):
            khan_votes += 1
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1
            
    #Calculate Percentage of Votes Won Per Candidate
    khan_percent = ((khan_votes/total_votes) * 100) 
    correy_percent = ((correy_votes/total_votes) * 100) 
    li_percent = ((li_votes/total_votes) * 100)
    otooley_percent = ((otooley_votes/total_votes) * 100) 
    
    #Round Percentage to 3 Decimal Places
    khan_percent = "%.3f%%" % khan_percent 
    correy_percent = "%.3f%%" % correy_percent
    li_percent = "%.3f%%" % li_percent 
    otooley_percent = "%.3f%%" % otooley_percent

    #Calculate Winner
    winner = max(khan_votes, correy_votes, li_votes, otooley_votes)

    if winner == khan_votes:
        winner_name = "Khan"
    elif winner == correy_votes:
        winner_name = "Correy"
    elif winner == li_votes:
        winner_name = "Li"
    else:
        winner_name = "O'Tooley" 

#Print Election Results
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------------")
print(f"Khan: {khan_percent} ({khan_votes})")
print(f"Correy: {correy_percent} ({correy_votes})")
print(f"Li: {li_percent} ({li_votes})")
print(f"O'Tooley: {otooley_percent} ({otooley_votes})")
print(f"---------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------")

#Create Text File (Election Results)
output = os.path.join("..", "Analysis", 'Election_Results.txt')
with open(output, 'w') as text_file:
    text_file.write("Election Results")
    text_file.write("\n")
    text_file.write("------------------------")
    text_file.write("\n")
    text_file.write(f"Total Votes: {total_votes}")
    text_file.write("\n")
    text_file.write("------------------------")
    text_file.write("\n")
    text_file.write(f"Khan: {khan_percent} ({khan_votes})")
    text_file.write("\n")
    text_file.write(f"Correy: {correy_percent} ({correy_votes})")
    text_file.write("\n")
    text_file.write(f"Li: {li_percent} ({li_votes})")
    text_file.write("\n")
    text_file.write(f"O'Tooley: {otooley_percent} ({otooley_votes})")
    text_file.write("\n")
    text_file.write("------------------------")
    text_file.write("\n")
    text_file.write(f"Winner: {winner_name}")
    text_file.write("\n")
    text_file.write("------------------------")

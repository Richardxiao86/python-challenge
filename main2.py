# Start command
import pandas as pd
from pathlib import Path 

# Read and define CSV file
csv_file_path = Path("PyPoll","Resources",election_data.csv")

# Define Variables 
t_votes = 0 
k_votes = 0
c_votes = 0
l_votes = 0
o_votes = 0

# Define elections
with open(csv_file_path,newline="", encoding="utf-8") as elections:

    # Store data as a variable
    csv_reader = csv.reader(elections,delimiter=",") 


    # Define each row in the csv
    for row in csvreader: 

        # identify Voter ID's and give it to a variable  called t_votes
        t_votes +=1

        # define other rows
        if row[2] == "Khan": 
            k_votes +=1
        elif row[2] == "Correy":
            c_votes +=1
        elif row[2] == "Li": 
            l_votes +=1
        elif row[2] == "O'Tooley":
            o_votes +=1

 # Define two dictioaries
Lists  = ["Khan", "Correy", "Li","O'Tooley"]
 Variables= [k_votes, c_votes,l_votes,o_votes]

# Merge the lists with variables
# get the winner through a max function of the dictionary 
dict_lists_and_variables = dict(zip(lists,variables))
max_value= max(dict_lists_and_variables, max_value=dict_lists_and_variables.get)

# Get the percentage for each candidate
k_percent = (k_votes/t_votes) *100
c_percent = (c_votes/t_votes) * 100
l_percent = (l_votes/t_votes)* 100
o_percent = (o_votes/t_votes) * 100

# Print the table
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {t_votes}")
print(f"----------------------------")
print(f"Khan: {k_percent:.3f}% ({k_votes})")
print(f"Correy: {c_percent:.3f}% ({c_votes})")
print(f"Li: {l_percent:.3f}% ({l_votes})")
print(f"O'Tooley: {o_percent:.3f}% ({o_votes})")
print(f"----------------------------")
print(f"Winner: {max_value}")
print(f"----------------------------")

# Output of outcome
output_file = Path("PyPoll","Resources", "Election_Results.txt")

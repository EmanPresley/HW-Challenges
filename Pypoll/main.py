# Import module
import os
import csv

# Set path
election_data = "Resources/election_data.csv"

# set variables
total_votes = 0
total_candidates = 0

# set variables for counting/changes
changes = []
votes = 0
# candidates = []
all_candidates = {}
last_vote = 0
last_candidate= 0
min_vote = 999999999
max_vote = -999999999
min_candidates = -1
max_candidates = 1000



# open the CSV
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
     # need to skip the header
    # read each row of data after the header
    csv_header = next(csvreader)

    
    for row in csvreader:
            
            # Analyze the votes and calculate the total number of votes cast
            if total_votes != 0:
                change = int(row[0]) - last_vote
                changes.append(change)

                # check max/min change
                if change > max_vote:
                    max_vote = change
                    votes = row[1]
                else:
                    pass
            
            # add vote counter
            total_votes = total_votes + 1

            # Calculate a complete list of candidates who received votes
            # Credit to prof Booth for replacement code over the `not in` if statement commented out below
            candidate = row[2]

            if candidate in all_candidates.keys():
                all_candidates[candidate] += 1
            else:
                all_candidates[candidate] = 1
                
print("Election Results:")
# make it print out nicely
print("------------------------------------")

# Calculate the total number of votes each candidate won
print(f"Total votes: {total_votes}")
print("------------------------------------")    

# credit for colum printing found @https://bobbyhadz.com/blog/python-print-dictionary-in-table-format
headers=["Name", "Votes"]
for key, value in all_candidates.items():
    print(f'{key:} {value:}')
print("------------------------------------") 

       
        # # Calculate a complete list of candidates who received votes
        # # credit for `not in` if statement goes to Chris H. 
        # # @ https://stackoverflow.com/questions/19834806/is-there-a-more-pythonic-way-to-prevent-adding-a-duplicate-to-a-list
        #     if row[2] not in candidates:
        #         # add candidate
        #         candidates.append(row[2])
        #     else:
        #         pass
         
# # print(f"List of candidates who received votes: {candidates}")



# Calculate the percentage of votes each candidate won
perc_dict = {}
total = sum(all_candidates.values())
for key,val in all_candidates.items():
    perc_dict[key] = str(round(val/total * 100, 2)) + '%'
    

for key, value in perc_dict.items():
    print(f'{key:} {value:}')
print("------------------------------------") 

# Calculate the winner of the election based on popular vote    
def winner(d):
  return max(d, key = d.get)


print(f"Winner:")
print(winner(all_candidates))

election_w = (winner(all_candidates))
# print (election_w)
#  analysis should align with the following results:
# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------

# Final script should both print the analysis to the terminal and export a text file with the results
# Final script should both print the analysis to the terminal and export a text file with the results
with open("output_pypoll.txt", "w", encoding='utf-8') as txt_file:
    output = f"""
Election Results:
----------------------------
Total Votes: {total_votes}
----------------------------
Candidates: {all_candidates}
----------------------------
Percent of Votes Won: {perc_dict}
----------------------------
Winner of Election: {election_w}"""

    txt_file.write(output)
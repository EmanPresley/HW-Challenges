# Import Module
import os
import csv

# Set path
budget_data = "Resources/budget_data.csv"

# set varaiables
total_months = 0
total_profit_loss = 0

# set variables for the changes
# credit to prof booth for changes code
changes = []
last_profit_loss = 0
min_change = 999999999
max_change = -999999999
min_month = ""
max_month = ""


# Open the CSV using the UTF-8 encoding
with open(budget_data, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


    
    # need to skip the header
    # read each row of data after the header
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    for row in csvreader:
        print(row)
        
        # Calculate the changes in "Profit/Losses" over the entire period, and then the average of those changes
        # changes
        # if first row, no change, but assign last_profit_loss
        # else, calculate the change

        if total_months != 0:
            change = int(row[1]) - last_profit_loss
            changes.append(change)

            # check max/min change
            if change > max_change:
                max_change = change
                max_month = row[0]
            elif change < min_change:
                min_change = change
                min_month = row[0]
            else:
                pass # do nothing, there is no change
        # add month counter
        total_months = total_months + 1
            
        # assign last month profit
        last_profit_loss = int(row[1])        
            
        # Calculate the net total amount of "Profit/Losses" over the entire period
        total_profit_loss = total_profit_loss + int(row[1])  
        
# calculate the total number of Months        
total_num_months = f"Total number of months:{total_months}"
print(total_num_months)

print(f"Total: ${total_profit_loss}")  

# Calculate average change
avg_change = sum(changes) / len(changes)
print(f"Average change: ${round(avg_change, 2)}")

# Calculate The greatest increase in profits (date and amount) over the entire period
print(f"Greatest increase in Profits: ${max_change} in {max_month}")  
      
 # Calculate the greatest decrease in profits (date and amount) over the entire period
print(f"Greatest decrease in profits: ${min_change} in {min_month}")


# Analysis should align with the following results:
# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)

# Final script should both print the analysis to the terminal and export a text file with the results
with open("output_pybank.txt", "w") as txt_file:
    output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${total_profit_loss}
Average Change: ${round(avg_change, 2)}
Greatest Increase in Profits: {max_month} (${max_change})
Greatest Decrease in Profits: {min_month} (${min_change})"""

    txt_file.write(output)
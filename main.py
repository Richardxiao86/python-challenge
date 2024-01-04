# Import path
import pandas as pa
from pathlib import Path 

# Find file location 
df = Path("PyBank", "resources", "budget_data.csv")

# set up the total months and profit
t_months = []
t_profit = []
m_profit_change = []
 
# Open csv and define variables
with open(df,newline="", encoding="utf-8") as budget:

     # Store the contents of budget_data.csv in  csvreader
    csvreader = csv.reader(budget,delimiter=",") 

 

    # creat the data for totoal satistics

        # Append the total months and total profit 
        t_months.append(row[0])
        t_profit.append(int(row[1]))

    # Get the monthly profits change
    for x in range(len(t_profit)-1):
        
        # Get the  monthly profits change through a function
        m_profit_change.append(t_profit[x+1]-t_profit[x])
        
# Get the maximum and minimum of values
max_increase_value = max(m_profit_change)
max_decrease_value = min(m_profit_change)

# Use monthly list and index from max and min to get the max increase month and decrease month

max_incr_month = m_profit_change.index(max(m_profit_change)) + 1
max_decr_month = m_profit_change.index(min(m_profit_change)) + 1 

# Print Statements

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(t_months)}")
print(f"Total: ${sum(t_profit)}")
print(f"Average Change: {round(sum(m_profit_change)/len(m_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_incr_month]} (${(str(max_increase_value))})")
print(f"Greatest Decrease in Profits: {total_months[max_decr_month]} (${(str(max_decrease_value))})")

# Output files
output_file = Path("starter_code(1)", "PyBank", "Financial_Analysis.txt")

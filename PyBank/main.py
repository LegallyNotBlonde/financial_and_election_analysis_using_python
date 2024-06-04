#import os to use operating system to work with files and folders
import os
#imprts scv to be able to work with scv files
import csv

#set path the to file with the data
csvpath = r'Resources\budget_data.csv'


# Set variables
total_months = 0
total_profit = 0
previous_profit = 0

# this is a list with no values assigned. The list is needed as we need to store profit changes for each month and then find a greatest inctease and descrease
profit_changes = []

# variabes without set values as we want to assign them. The variables will stay blank until the largest increases and decreases in profit are found
date_greatest_increase = ""
date_greatest_decrease = ""

# Find the greatest increase and decrease in profits. 'Inf' helps to identify that decrease is neagative, plus it helps to  to ensure that a variable starts with a value that is guaranteed to be replaced by actual data during the analysis.

greatest_increase = float('-inf')
greatest_decrease = float('inf')

# Activate the csv module to read the CSV file. Delivemter is used to split information the 1st column (separate day and month)
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # Create a loop to go through each line in the csv file

    for row in csvreader:
        #identify where is this file we store date and profit
        date = row[0]
        profit = int(row[1])

        #To increase the total number of months by 1 for each iteration of the loop
        total_months += 1

        #create conditiona that starts only after the 1st month
        if total_months > 1:
            #to count the profit change between the current and the previous months
            profit_change = profit - previous_profit

            #to add the profit change to the list (we declared it above wiht no value as [])
            profit_changes.append(profit_change)

            #to check if the current profit change is the largest (greatest) change
            if profit_change > greatest_increase:
                #if condition is met, then greatest _increase and date_greatest_increase get values assigned respectively
                greatest_increase = profit_change
                date_greatest_increase = date

            #to check if the current profit change is the greatest decrease and assign values if condition is met
            if profit_change < greatest_decrease:
                greatest_decrease = profit_change
                date_greatest_decrease = date

        #to increase the total profit by the current profit
        total_profit += profit
        #to update the previous profit for the next iteration of the loop
        previous_profit = profit

#to count an average profit change
average_change = round(sum(profit_changes) / len(profit_changes), 2)

#to print required results in the certain format, based on the screenshot in the challenge 3
print("Financial Analysis")
print("-------------------------")
print("Total Months:", total_months)
print("Total: $" + str(total_profit))
print("Average Change: ${:,.2f}".format(average_change))
print("Greatest Increase in Profits:", date_greatest_increase, "($" + str(greatest_increase) + ")")
print("Greatest Decrease in Profits:", date_greatest_decrease, "($" + str(greatest_decrease) + ")")


# to export the analysis results to the text file

output_file_path = "financial_analysis.txt"
with open(output_file_path, "w") as file:
    file.write("Financial Analysis\n")
    file.write("-------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit}\n")
    file.write(f"Average Change: ${average_change}\n")
    file.write("Greatest Increase in Profits: " + str(date_greatest_increase) + " ($" + str(greatest_increase) + ")\n")
    file.write("Greatest Decrease in Profits: " + str(date_greatest_decrease) + " ($" + str(greatest_decrease) + ")\n")

print(f"Analysis results have been exported to {output_file_path}")






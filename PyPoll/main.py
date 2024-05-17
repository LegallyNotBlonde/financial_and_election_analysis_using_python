#import module operating system module to work with files
import os
#import csv to work with csv files
import csv

#setting the path to the file with the data
csvpath = r'Resources\election_data.csv'

#we need to count the number of votes  and determine which candidates received support
#counting the number of unique vote IDs will allow us to do that

unique_ids = set()  # this set stores unique vote/ballot ID
unique_candidates = set()  #this set stores unique candidate names

# set dictionary to store candidate names and their respective vote counts
#dictionary seems to be the better option to determine needed value based on the known key in a large data set
candidate_votes = {}  

# open the CSV file using open function
with open(csvpath) as csvfile:

    # create a CSV reader object
    csvreader = csv.reader(csvfile)

    # skip the header row
    next(csvreader)

    # iterate through each row in the CSV file
    for row in csvreader:

        # extract the ballot ID from the first column (0 index)
        ballot_id = row[0]

        # add the ballot ID to the set of unique IDs
        unique_ids.add(ballot_id)

        # extract the candidate name from the third column 
        candidate_name = row[2]

        # add the candidate name to the set of unique candidates
        unique_candidates.add(candidate_name)

        # count the votes for each candidate
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

# Count the total number of votes cast
total_votes = len(unique_ids)

# Print the total number of votes
print("Elections Results")
print("-------------------------")
print("Total Votes:", total_votes)
print("-------------------------")

# Print the list of unique candidates who received votes and their respective vote counts
print 
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("-------------------------")

# Find the candidate with the highest number of votes
winner = max(candidate_votes, key=candidate_votes.get)

# Print the winner
print("Winner:", winner)

print("-------------------------")


# Open the file using "write" mode. Specify the variable to hold the contents
with open("election_results.txt", "w") as file:
    # Write the results to the file
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write("Total Votes: " + str(total_votes) + "\n")
    file.write("-------------------------\n")
     # Iterate through the dictionary items and calculate percentage
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        # Write the output to the file
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write("Winner: " + winner + "\n")


# Print a message to confirm that the results have been exported
print("Results have been exported to election_results.txt")
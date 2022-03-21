# The data we need to retrieve
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

# Import the datetime class from the datetime module.
#import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
# now = dt.datetime.now()
# Print the present time.
# print("The time right now is ", now)

import csv
import os

# Assign a variable to load a file from a path
# direct path
# file_to_load = 'Resources/election_results.csv'
# indirect path
file_to_load = os.path.join("Resources","election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    #for row in file_reader:
    #    print(row)


# Using the with statement open the file as a text file
#with open(file_to_save, "w") as txt_file:
    # Write some data to the file.
    #txt_file.write("Arapahoe\nDenver\nJefferson")











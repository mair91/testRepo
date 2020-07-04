import os
import csv
# Path to collect data from the Resources folder
wrestling_csv =  os.path.join("Resources","WWE-Data-2016.csv")

# Define the function and have it accept the 'wrestlerData' as its sole parameter
def print_percentages(row):
# Find the total number of matches wrestled
    total = int(row[1])+int(row[2])+int(row[3])
    name = row[0]
# Find the percentage of matches won
    pw = "{:.0%}".format(int(row[1])/total)
# Find the percentage of matches lost
    pl = "{:.0%}".format(int(row[2])/total)
# Find the percentage of matches drawn
    pd = "{:.0%}".format(int(row[3])/total)
# Print out the wrestler's name and their percentage stats
    print(f'{name}  Wins:{pw}  Lost:{pl}  Draw:{pd}')
# Read in the CSV file

with open(wrestling_csv, 'r') as csvfile:

# Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

# Prompt the user for what wrestler they would like to search for
    name_to_check = input("What wrestler do you want to look for? ")

# Loop through the data
    for row in csvreader:
# If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if(name_to_check == row[0]):
            print_percentages(row)

#Import os (create file paths)
import os

#Import csv to read csv files
import csv

csvpath = os.path.join('Resources','election_data.csv')

# Read CSV using CVS Module

with open (csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',') 

    # Create lists and variable to store data
    numberVotes = 0
    candidates = []
    numVotes = []
    votesPercentage = []

    #Skip two rows, as there is a <<<<<<< HEAD and a header
    coso = next(csvreader)
    coso = next(csvreader)
    
    # Create a for loop to iterate through all the rows of the cvs
    for coso in csvreader:

        #Each iteration = 1 vote
        numberVotes += 1
        # The value of candidate is equal to the value of the second "column"
        candidate = coso[2]
        
        # If candidate is not in list, add it, and append a new item to the list numVotes (in the same position that candidate in candidates)
        if candidate not in candidates:
            candidates.append(candidate)
            numVotes.append(1)

        # If candidate is already in list, add one to the item in the same position in the list numVotes.
        elif candidate in candidates:
            position = candidates.index(candidate)
            numVotes[position] += 1

# Compensate for extra iteration.
    numberVotes = numberVotes - 1

# Find the percentage of votes and rounding them to two decimals
    
votesPercentage = [((i /numberVotes) * 100) for i in numVotes]

votesPercentage = [round(i,2)for i in votesPercentage]

# Finding the winner
winnerV = max(numVotes)

# Find the position of the winner and the winner's votes
winnerPosition = numVotes.index(winnerV)
winnerC = candidates[winnerPosition]  


Results = (f" Election Results \n -------------------- \n Total Votes: {numberVotes} \n -------------------- \n ")




print(numVotes)
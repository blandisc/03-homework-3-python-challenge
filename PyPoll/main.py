#Import os (create file paths)
import os

#Import csv to read csv files
import csv

csvpath = os.path.join('Resources','election_data.csv')

# Read CSV using CVS Module

with open (csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',') 
    # Turn CSV into List
    cleanData = list(csvreader)

    #Delete headers and last row
    del cleanData[0:2]
    del cleanData[-1]
    print(len(cleanData))
    
    #Create new CVS "clean"file
with open('election_data_clean.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(cleanData)

    # Open CSV clean file
csvpath = os.path.join('election_data_clean.csv')

# Read CSV using CVS Module

with open (csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',') 
    #Create lists and variable to store data
    numberVotes = 0
    candidates = []
    numVotes = []
    votesPercentage = []


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


# Find the percentage of votes and rounding them to two decimals
    
votesPercentage = [((i /numberVotes) * 100) for i in numVotes]

votesPercentage = [round(i,2)for i in votesPercentage]

# Finding the winner
winnerV = max(numVotes)

# Find the position of the winner and the winner's votes
winnerPosition = numVotes.index(winnerV)
winnerC = candidates[winnerPosition]  


Results = (f" Election Results \n -------------------- \n Total Votes: {numberVotes} \n -------------------- \n {candidates[1]} : {numVotes[1]} \n  ")

# Print Results into txt file and print them in terminal
file = open("Results.txt","w")
file.write(Results)
file.close()

print(Results)
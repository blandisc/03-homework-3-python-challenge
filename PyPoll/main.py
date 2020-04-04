#Import os (create file paths)
import os

#Import csv to read csv files
import csv

csvpath = os.path.join('Resources','02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')

# Read CSV using CVS Module
with open (csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',') 
    # Turn CSV into List
    cleanData = list(csvreader)

    #Delete headers and last row
    del cleanData[0:2]
    del cleanData[-1]

    lengths = [len(i) for i in cleanData]

    lenght = (min(lengths))

    errorPosition =lengths.index(lenght)

    del cleanData [errorPosition: errorPosition + 2]

#Indicate path for new file
csvpathClean = os.path.join('Resources','election_data_clean.csv')

#Create new CVS "clean"file
with open(csvpathClean, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(cleanData)

# Open CSV clean file
csvpath = os.path.join('Resources','election_data_clean.csv')

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

# Create the Results
Results = (
            f" Election Results \n -------------------- \n" 
            f" Total Votes: {numberVotes} \n -------------------- \n" 
            f" {candidates[0]}: {votesPercentage[0]}% ({numVotes[0]}) \n"
            f" {candidates[1]}: {votesPercentage[1]}% ({numVotes[1]}) \n" 
            f" {candidates[2]}: {votesPercentage[2]}% ({numVotes[2]}) \n" 
            f" {candidates[3]}: {votesPercentage[3]}% ({numVotes[3]}) \n"
            f" -------------------- \n" 
            f" Winner: {winnerC} \n"
            f"-------------------- ")

# Print Results into txt file and print them in terminal
file = open("ResultsPyPoll.txt","w")
file.write(Results)
file.close()

print(Results)
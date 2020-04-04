#Import os (create file paths)
import os

#Import csv to read csv files
import csv

csvpath = os.path.join('Resources','budget_data.csv')

# Read CSV using CVS Module

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # Insert CSV in Dictionary
    data = dict(csvreader)
    # profitsLosses = dict(csvreader)

    # Deleting the first Key and Value
    del data['Date']

    # Converting values into int
    for values in data: 
        data[values] = int(data[values]) 

    # Counting the number of Keys using len() and placing them in variable numberDates
    numberDates = len(data)

    # Adding all the profits and losses
    financialResults = sum(data.values())

    # Convert Dict into list to obtain increases and decreses
    data2 = list(data.values())
    data3 = list(data.keys())
    
    # Deleting first month (can't delete from data2 as it would break code on line 45)
    del data3 [0]
   

    # Create list to contain changes
    changes = []

    #Create for loop to obtain differences between periods (starting from 1 and not 0 because we don't have change for period 0) and append them into changes list
    for x in range(1,numberDates):
            changes.append(data2[x]-data2[x-1])

    #Obtain the average change  and round it to two decimals
    changeAverage = round(sum(changes)/len(changes),2)

    #Obtain the period with the greatest increase in profits
    maxChange = max(changes)

    #Obtain the position of the greatest increase
    maxChangeposition = changes.index(maxChange)
    monthmax = data3[maxChangeposition]

    #Obtain the period with the greatest decrease in profits
    maxChangeD = min(changes)

    #Obtain the position of the greatest decrease
    maxChangepositionD = changes.index(maxChangeD)
    monthmaxD = data3[maxChangepositionD]

Results = (f"Financial Analysis \n -------------------- \n Total Months: {numberDates} \n Total : ${financialResults} \n Average Change: $ {changeAverage} \n Greatest Increase in Profits: {monthmax} ${maxChange} \n Greatest Decrease in Profits: {monthmaxD} ${maxChangeD}")

# Print Results into txt file and print them in terminal
file = open("ResultsPyBank.txt","w")
file.write(Results)
file.close()

print(Results)

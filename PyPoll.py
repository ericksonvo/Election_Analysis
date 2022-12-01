# The data we need to receive
# 1. The total number of vote casted
# 2. Complete list of candidate names
# 3. The percentage of votes each canidate won
# 4. Total number of votes each candidate won
# 5. The winner of the election based on popular vote

#indirect way to open files using the os.path.join() 

## add our dependencies
import csv
import os

## Assign a varible to load a file from a path
file_to_load=os.path.join("Resources","election_results.csv")


## Assign a varible to save the file to path.
file_to_save=os.path.join("analysis","election_analysis.txt")

## open election results and read file.
with open(file_to_load) as election_data:

## read the file object with reader function.
        file_reader = csv.reader(election_data)

##print each row in the CSV file
        headers = next(file_reader)
        print(headers)

# use the open statement to open the file as a text file.
with open(file_to_save,"w") as txt_file:
# write some data to the file
        txt_file.write("Counties in the Election")
        txt_file.write("\n________________________")
      
# add three counties to the file
        txt_file.write("\nArapahoe\nDenver\nJefferson")
        
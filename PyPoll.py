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
file_to_save=os.path.join("analysis","election_analysis.txt")
# Assign a varible to load a file from a path
file_to_load=os.path.join("Resources","election_results.csv")


#  Assign a varible to save the file to path.
file_to_save=os.path.join("analysis","election_analysis.txt")

#### 1. accumulator: initialize total_votes to 0
total_votes=0
## 1. adding candidate option
candidate_option=[]
## create candidate and vote dictionary
candidate_votes={}
# creating variables for candidatea and winning count tracker, by declaring the variable to hold empty strings
winning_candidate= ""
winning_count=0
winning_percentage=0
### open election results and read file.
with open(file_to_load) as election_data:

###### read the file object with reader function.
        file_reader = csv.reader(election_data)

 ###### read the header row
        headers = next(file_reader)
 ## print each row in the CVS file
        for row in file_reader:
                #### 2. Add the total vote count
                total_votes+= 1
                # print candidate name
                candidate_name=row[2]
                # if candidate does not match any existing candidate
                if candidate_name not in candidate_option:
                # add candidate name to candidate option
                   candidate_option.append(candidate_name)

                # track each candidate vote count by creating key using dictionary_name[key], setting it to 0 will set each vote count back to 0
                   candidate_votes[candidate_name] = 0
# to incremenet each candidate vote we need to move the vote counter inside the for loop (align it with the if statement)
                candidate_votes[candidate_name] +=1 
3#save the results to our text file
with open(file_to_save,"w") as txt_file:
# print the final vote count to the terminal
        election_results =(f"\nElection Results\n" 
                           f"------------------------\n"
                           f"Total voltes:{total_votes:,}\n"
                           f"-------------------------\n")
        print(election_results,end="")
        # save the final vote count to the text file
        txt_file.write(election_results)
        for candidate_name in candidate_votes:
                # 2. Retreieve vote count of candidate
                votes=candidate_votes[candidate_name]
                # 3. Calculate the percentage of votes using float
                vote_percentage=float(votes)/float(total_votes) * 100
                # ** round the percentage to one decimal place. 
                # 4. print using f "candidate name: received % of the vote"
                candidate_results=(f"{candidate_name:}: {vote_percentage:.1f}% ({votes:,})\n")     
                # determine the winning vote count and candidatee using if statement
                print(candidate_results)
                txt_file.write(candidate_results)
                
                if (votes>winning_count) and (vote_percentage>winning_percentage): 
                        # if true then set winning count = to votes and winning percentage = vote percentage
                        winning_count=votes
                        winning_percentage=vote_percentage
                        winning_candidate=candidate_name
        ## print out each canidates name, vote count and percentage of votes
        winning_candidate_summary=(
                f"--------------------------\n"
                f"winnner:{winning_candidate}\n"
                f"Winning Vote Count: {winning_count,}\n"
                f"winning percentage: {winning_percentage:.1f}%\n"
                f"---------------------------\n") 
        print(winning_candidate_summary)     
        txt_file.write(winning_candidate_summary)  



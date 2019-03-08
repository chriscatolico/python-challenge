import csv
import os

electionData_csv = os.path.join("election_data.csv")

#open csv file and count total lines to find total votes
with open(electionData_csv, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	csv_header = next(csvfile)
	
	line_count = sum(1 for line in csvreader)

print('Election Results\n---------------------')
print(f'Total Votes: {line_count}\n---------------------')

#open csv file, create a list of candidates, and remove duplicates from list
with open(electionData_csv, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter=',')
	csv_header = next(csvfile)
	
	listofCandidates = []

	for line in csvreader:
		candidateName = line[2]
		listofCandidates.append(candidateName)

listofCandidates = list(set(listofCandidates)) #remove duplicates from list


#function to count candidate vote based on index from list of candidates
def candidateCounter(candidateIndex):
	
	vote_counter = 0

	with open(electionData_csv, newline='') as csvfile:
		csvreader = csv.reader(csvfile, delimiter=',')
		csv_header = next(csvfile)

		for line in csvreader:
			if line[2] == listofCandidates[candidateIndex]:
				vote_counter += 1
		return vote_counter

#create a dictionary with candidates and respective votes
dict_results={}
for candidate_index in range(len(listofCandidates)):
	result = candidateCounter(candidate_index)
	candidateName = listofCandidates[candidate_index]
	dict_results[candidateName] = result

#loop through dictionary to give candidate and vote result
for person,votes in dict_results.items():
	print(f'{person}: {round((votes/line_count*100),3)}% ({votes})')


#print winner by finding max value in dictionary and return the relative key
print('---------------------\n'+'Winner: ' + max(dict_results, key=dict_results.get))

#code should work with varying data in same format!
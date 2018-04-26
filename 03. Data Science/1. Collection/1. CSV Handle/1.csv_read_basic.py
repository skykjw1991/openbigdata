import csv

with open('Demographic_Statistics_By_Zip_Code.csv', newline="") as infile:
    data = list(csv.reader(infile))

countParticipantsIndex = data[0].index("COUNT PARTICIPANTS")
print("The index of 'COUNT PARTICIPANTS': "+str(countParticipantsIndex))

countParticipants =[]
# index =0

for row in data[1:]:
    countParticipants.append(row[countParticipantsIndex])

print("<COUNT PARTICIPANT>")
for participant in countParticipants:
    print(participant)
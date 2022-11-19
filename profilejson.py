from fuzzywuzzy import fuzz
import csv
import json

with open('Metadata.csv') as csvfile:
    Data = []

    csvreader = csv.reader(csvfile , delimiter=',')
    # skips your header
    next(csvreader)
    for row in csvreader:
        Data.append({
            'name': row[0],
            'id': row[1]
        })

print(Data[:10])
with open('yourjson.json', 'w') as f:
    # indent does the prettify
    json.dump(Data, f, indent=4)
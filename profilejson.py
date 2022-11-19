import csv
import json
import pandas as pd

with open('Metadata.csv') as csvfile:
    Data = []
    csvreader = csv.reader(csvfile , delimiter=',')
    # skips your header
    next(csvreader)
    for row in csvreader:
        clubs = []
        Data.append({
            'name': row[0],
            'id': row[1],
            'clubs': {
                'club_i': {
                'isOrganiser': 'Organiser',
                'club_i_event_j': {
                    'participated': False
                    },
                },
            },
            'fests': {
            'fest_i': {
                'isOrganiser': '',
                'fest_i_event_j': {
                    'participated': True
                    },
            },
            

            
        }
        })


print(Data[:1])
with open('Profilejson.json', 'w') as f:
    # indent does the prettify
    json.dump(Data, f, indent=4)
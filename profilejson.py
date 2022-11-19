import csv
import json
import pandas as pd

sortread = pd.read_csv("DefuzzifiedClubs_data.csv")
sortread.sort_values(["Name"],axis=0,ascending=[True],inplace=True)
sortread.to_csv("SortedDefuzzified.csv",index=False)



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
with open('yourjson.json', 'w') as f:
    # indent does the prettify
    json.dump(Data, f, indent=4)
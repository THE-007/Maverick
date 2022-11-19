import csv
import json
import pandas as pd
import os
data_path = 'fuzzy_csv'

sortread = pd.read_csv("/Users/himavanthkandula/Documents/GitHub/Maverick/defuzzy_csv/Clubs_data.csv")
sortread.sort_values(["Name"],axis=0,ascending=[True],inplace=True)
sortread.to_csv("/Users/himavanthkandula/Documents/GitHub/Maverick/defuzzy_csv/Clubs_data.csv",index=False)

sortread = pd.read_csv("/Users/himavanthkandula/Documents/GitHub/Maverick/defuzzy_csv/Organisers_In_Fests.csv")
sortread.sort_values(["Name"],axis=0,ascending=[True],inplace=True)
sortread.to_csv("/Users/himavanthkandula/Documents/GitHub/Maverick/defuzzy_csv/Organisers_In_Fests.csv",index=False)

sortread = pd.read_csv("/Users/himavanthkandula/Documents/GitHub/Maverick/defuzzy_csv/Participants_In_Fests.csv")
sortread.sort_values(["Name"],axis=0,ascending=[True],inplace=True)
sortread.to_csv("/Users/himavanthkandula/Documents/GitHub/Maverick/defuzzy_csv/Participants_In_Fests.csv",index=False)

sortread = pd.read_csv("//Users/himavanthkandula/Documents/GitHub/Maverick/Metadata.csv")
sortread.sort_values(["Name"],axis=0,ascending=[True],inplace=True)
sortread.to_csv("/Users/himavanthkandula/Documents/GitHub/Maverick/Metadata.csv",index=False)
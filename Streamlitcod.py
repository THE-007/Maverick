import streamlit as st
import pandas as pd
import numpy as np
##########################################################################################################################################
Metadata = pd.read_csv("Metadata.csv")
clubs = pd.read_csv("defuzzy_csv/Organisers_In_Fests.csv")
Organisers_in_fest = pd.read_csv("defuzzy_csv/Organisers_In_Fests.csv")
Participants_in_fests = pd.read_csv("defuzzy_csv/Participants_In_Fests.csv")

##########################################################################################################################################
Distinct_Clubs_Count = 3
Distinct_Fests_Count = 2
Distinct_Clubsevent_Count = [3,3,3]
Distinct_FestEvent_Count = [13,15]
##########################################################################################################################################
st.title("Dashboard")
##########################################################################################################################################
# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done!")
##########################################################################################################################################
if st.checkbox('Show Metadate'):
    st.subheader('Metadata')
    st.write(Metadata)
if st.checkbox('Show Clubs_data'):
    st.subheader('Clubs Data')
    st.write(clubs)
if st.checkbox('Show Organisers in Fest'):
    st.subheader('Organisers in Fest')
    st.write(Organisers_in_fest)
if st.checkbox('Show Participants in Fests'):
    st.subheader('Particpants in fest')
    st.write(Participants_in_fests)
##########################################################################################################################################
club_person_count = []
for i in range(Distinct_Clubs_Count):
    clubs_iter = clubs.loc[clubs['Club_Name'] == 'club_'+str(i+1)]
    clubs_iter = clubs_iter["Name"].unique()
    club_person_count.append((int(len(clubs_iter))))
##########################################################################################################################################
club_event_count = []
for i in range(int(Distinct_Clubs_Count)):
    club_event_iter = []
    for j in range(int(Distinct_Clubsevent_Count[i])):
        clubs_iter = clubs.loc[clubs['Event'] == 'club_'+str(i+1)+'_event_'+str(j+1)]
        clubs_iter = clubs_iter["Name"].unique()
        club_event_iter.append((int(len(clubs_iter))))
    club_event_count.append(club_event_iter)
##########################################################################################################################################
fests = pd.read_csv("Participants_In_Fests.csv")
fest_person_count = []
for i in range(Distinct_Clubs_Count):
    fests_iter = fests.loc[fests['Fest_Name'] == 'fest_'+str(i+1)]
    fests_iter = fests_iter["Name"].unique()
    fest_person_count.append((int(len(fests_iter))))
##########################################################################################################################################
fest_event_count = []
for i in range(int(Distinct_Fests_Count)):
    fest_event_iter = []
    for j in range(int(Distinct_FestEvent_Count[i])):
        fests_iter = fests.loc[fests['Event'] == 'fest_'+str(i+1)+'_event_'+str(j+1)]
        fests_iter = fests_iter["Name"].unique()
        fest_event_iter.append((int(len(fests_iter))))
    fest_event_count.append(fest_event_iter)

print(club_person_count)
print(club_event_count)
print(fest_person_count)
print(fest_event_count)

import pandas as pd
import numpy as np
st.subheader("CLUBS")
chart_data = pd.DataFrame(
    club_person_count,
    columns=["Students"])
print(chart_data)
st.bar_chart(club_person_count)


chart_data1 = pd.DataFrame(
    club_event_count,
    columns=["Event1","Event2","Event3"])
print(chart_data1)
st.bar_chart(data=chart_data1)

st.subheader("Fests")
chart_data2 = pd.DataFrame(
    fest_person_count,
    columns=["Persons"])
print(chart_data2)
st.bar_chart(data=chart_data2)

chart_data3 = pd.DataFrame(
    fest_event_count,
    columns=["Event_1","Event_2","Event_3","Event_4","Event_5","Event_6","Event_7","Event_8","Event_9","Event_10","Event_11","Event_12","Event_13","Event_14","Event_15"])
print(chart_data3)
st.bar_chart(data=chart_data3)
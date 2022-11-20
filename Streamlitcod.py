import streamlit as st
import pandas as pd
import numpy as np
##########################################################################################################################################
Metadata = pd.read_csv("Metadata.csv")
clubs = pd.read_csv("defuzzy_csv/Clubs_data.csv")
Organisers_in_fest = pd.read_csv("defuzzy_csv/Organisers_In_Fests.csv")
Participants_in_fests = pd.read_csv("defuzzy_csv/Participants_In_Fests.csv")
Organisers_in_clubs = pd.read_csv("Organiser_Final.csv")
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
if st.checkbox('Show Organisers in Clubs'):
    st.subheader('Organisers in Clubs')
    st.write(Organisers_in_clubs)

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
fests = pd.read_csv("defuzzy_csv/Participants_In_Fests.csv")
fest_person_count = []
for i in range(Distinct_Fests_Count):
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
    columns=["Students"],
    index=["Club1","Club2","Club3"])
print(chart_data)
st.bar_chart(club_person_count)


chart_data1 = pd.DataFrame(
    club_event_count,
    columns=["Event1","Event2","Event3"],
    index=["Club1","Club2","Club3"])
print(chart_data1)
st.bar_chart(data=chart_data1)

st.subheader("Fests")
chart_data2 = pd.DataFrame(
    fest_person_count,
    columns=["Persons"],
    index=["Fest1","Fest2"])
print(chart_data2)
st.bar_chart(data=chart_data2)

chart_data3 = pd.DataFrame(
    fest_event_count,
    columns=["Event_1","Event_2","Event_3","Event_4","Event_5","Event_6","Event_7","Event_8","Event_9","Event_10","Event_11","Event_12","Event_13","Event_14","Event_15"],
    index=["Fest1","Fest2"])
print(chart_data3)
st.bar_chart(data=chart_data3)


#################################################################################################################################

DF_CLUBS = pd.read_csv("defuzzy_csv/Clubs_data.csv")
DF_CLUBS_LIST = DF_CLUBS["Name"].unique()
print(len(DF_CLUBS_LIST))
DF_Fests = pd.read_csv("defuzzy_csv/Participants_In_Fests.csv")
DF_Fests_LIST = DF_Fests["Name"].unique()
dups = DF_Fests.pivot_table(index = ['Name'], aggfunc ='size')
print(len(dups))
count_total_fests = 0
for i in range(len(dups)):
    count_total_fests=count_total_fests+dups[i]
count_total_fests
count_total_fests_inclubaswell = 0
for i in range(len(dups)):
    if(DF_Fests_LIST[i] in DF_CLUBS_LIST):
        count_total_fests_inclubaswell = count_total_fests_inclubaswell+dups[i]
print(count_total_fests_inclubaswell)

GRAPH_LIST = [[len(DF_CLUBS_LIST),len(Metadata)-len(DF_CLUBS_LIST)],[count_total_fests_inclubaswell,count_total_fests-count_total_fests_inclubaswell]]

print(GRAPH_LIST )

st.subheader("Stats")
chart_data4 = pd.DataFrame(
    GRAPH_LIST,
    columns=["Participating","Not Participating"],
    index=["CLUBS","Fest Event Registrations"])
print(chart_data4)
st.bar_chart(data=chart_data4)


#################################################################################################################################


DF_FESTS_1 = pd.read_csv("/Users/himavanthkandula/Downloads/Maverick-main/defuzzy_csv/Participants_In_Fests.csv")
DF_FESTS_LIST = DF_FESTS_1["Name"].unique()
print(len(DF_FESTS_LIST))

DF_CLUBS_1 = pd.read_csv("/Users/himavanthkandula/Downloads/Maverick-main/defuzzy_csv/Clubs_data.csv")
DF_CLUBS_LIST = DF_CLUBS_1["Name"].unique()
dups1 = DF_CLUBS_1.pivot_table(index = ['Name'], aggfunc ='size')
print(dups1)
print(len(DF_CLUBS_LIST))

count_total_clubs = 0
for i in range(len(dups1)):
    count_total_clubs=count_total_clubs+dups1[i]
count_total_clubs
count_total_clubs_infestaswell = 0
for i in range(len(dups1)):
    if(DF_CLUBS_LIST[i] in DF_FESTS_LIST):
        count_total_clubs_infestaswell = count_total_clubs_infestaswell+dups1[i]
print(count_total_clubs_infestaswell)

GRAPH_LIST_fest = [[len(DF_FESTS_LIST),len(Metadata)-len(DF_FESTS_LIST)],[count_total_clubs_infestaswell,count_total_clubs-count_total_clubs_infestaswell]]


print(GRAPH_LIST_fest )
st.subheader("Stats")
chart_data5 = pd.DataFrame(
    GRAPH_LIST_fest ,
    columns=["Participating","Not Participating"],
    index=["Fests","Club Event Registrations"])
print(chart_data5)
st.bar_chart(data=chart_data5)

#################################################################################################################################

People_participating_in_fests_and_clubs = set(DF_CLUBS_LIST).intersection(DF_Fests_LIST)
#print(People_participating_in_fests_and_clubs)
print(len(People_participating_in_fests_and_clubs))

Peopleinclubnotfest = [x for x in DF_CLUBS_LIST if x not in DF_Fests_LIST]
peopleinfestnotinclub = [x for x in DF_Fests_LIST if x not in DF_CLUBS_LIST ]
print(len(Peopleinclubnotfest))
print(len(peopleinfestnotinclub))

st.subheader("Stats")
chart_data6 = pd.DataFrame(
    [len(People_participating_in_fests_and_clubs),len(Peopleinclubnotfest),len(peopleinfestnotinclub)],
    columns=["Participating"],
    index=["BOTH","CLUBS NOT FEST","FEST NOT CLUB"])
print(chart_data6)
st.bar_chart(data=chart_data6)
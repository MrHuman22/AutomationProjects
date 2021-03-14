"""
Every event requires me to make x number of folders.
Extract file path from choose a folder using the PySimpleGUI browser and make a list of folders inside
Some Optional Folders

Folders:
/Event/
    - PRFs
    - Score Sheets
    - Guides
    - Attendance Sheets
    - Travel Diary
    - Certificates (Optional)
    - Trophy (Optional)

Also generates a packing list in my private Trello
"""

import PySimpleGUI as sg
import os
from enum import Enum
import requests
from decouple import config
import json
from datetime import datetime, timedelta


class Key(Enum):
    PATH = "PATH"
    CERTIFICATES = "CERTIFICATES"
    TROPHY = "TROPHY"
    START_DATE = "START_DATE"
    TRAVEL_DAYS_BEFORE = "TRAVEL_DAYS_BEFORE"
    TRAVEL_DAYS_AFTER = "TRAVEL_DAYS_AFTER"
    EVENT_DAYS = "EVENT_DAYS"
    SUBMIT = "SUBMIT"
    TRELLO_API_KEY = "TRELLO_API_KEY"
    TRELLO_TOKEN = "TRELLO_TOKEN"
    PRFS = "PRFs"

api_key = config(Key.TRELLO_API_KEY.value)
token = config(Key.TRELLO_TOKEN.value)
date_format = "%y-%m-%d"

folders = [
    "PRFs",
    "Score Sheets",
    "Guides",
    "Attendance Sheets",
    "Certificates",
    "Travel Diary",
    "Final Report"
]

layout = [[sg.Text("Choose an event folder:"),sg.FolderBrowse(key=Key.PATH.value)],
        [sg.CalendarButton(button_text="Travel Start Date", target=Key.START_DATE.value, format=date_format),sg.In(key=Key.START_DATE.value,enable_events=True,visible=True,size=(20,1))],
        [sg.Text("Travel Days before:"),sg.InputText(key=Key.TRAVEL_DAYS_BEFORE.value,size=(2,1)),sg.Text("Event Days:"),sg.InputText(key=Key.EVENT_DAYS.value,size=(2,1)),sg.Text("Travel Days After:"),sg.InputText(key=Key.TRAVEL_DAYS_AFTER.value,size=(2,1))],
        [sg.Checkbox("Trophy?",key=Key.TROPHY.value)],[sg.Checkbox("Certificates?",key=Key.CERTIFICATES.value)],
        [sg.Submit(key=Key.SUBMIT.value)]]

window = sg.Window("Generate Event Folders", layout)

while True:
    event, values = window.read()
    print(f"event: {event},values: {values}")
    if event == "Exit" or event == Key.SUBMIT.value or event== sg.WIN_CLOSED:
        window.close()
        break

if values[Key.TROPHY.value]:
    folders.append(Key.TROPHY.value.lower()),

if values[Key.CERTIFICATES.value]:
    folders.append(Key.CERTIFICATES.value.lower())

for k, v in values.items():
    print(f"{k}: {v}")

for each_folder in folders:
    print(f"Now adding {each_folder} into path")
    new_folder_path = os.path.join(values[Key.PATH.value],each_folder)
    print(new_folder_path)
    os.mkdir(new_folder_path)

# now adding the subfolders for each day in the PRF folder
# find the actual start date by taking the travel start date and adding travel_days_before
travel_start_date = datetime.strptime(values[Key.START_DATE.value],date_format)
event_start_date = travel_start_date + timedelta(days=int(values[Key.TRAVEL_DAYS_BEFORE.value]))
event_day_count = int(values[Key.EVENT_DAYS.value])
for x in range(event_day_count):
    event_date = event_start_date + timedelta(days=x)
    folder_name = event_date.strftime(date_format + " %a")
    # print(folder_name)
    new_subfolder_path = os.path.join(values[Key.PATH.value],Key.PRFS.value,folder_name)
    os.mkdir(new_subfolder_path)

# start_date = "21-03-15"
# travel_days = 1
# event_days = 4
# name = "Tamworth Packing List"
# id_list = "idList"

# # print(requests.get(f"https://api.trello.com/1/members/me/boards?key={api_key}&token={token}").json())
# def add_new_card(id_list:str,name: str,start_date: str,pos: str="top",id_labels:str ="Housework/Admin") -> None:
#     # take the due date and convert to datetime
#     due_date = datetime.strptime(start_date,date_format) - timedelta(days=1)
#     due_date_str = due_date.strftime(date_format)
#     print(f"start date: {start_date}, due_date: {due_date_str}")

#     params = {
#         "key" : api_key,
#         "token" : token,
#         "idList" : id_list,
#         "name" : name,
#         "due" : due_date_str,
#         "pos" : pos,
#         "idLabels" : "Housework/Admin"
#     }

#     for k, v in params.items():
#         print(f"{k}: {v}")

# add_new_card(id_list,name,start_date,)

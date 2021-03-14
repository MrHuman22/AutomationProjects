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

class Key(Enum):
    PATH = "PATH"
    CERTIFICATES = "CERTIFICATES"
    TROPHY = "TROPHY"
    START_DATE = "START_DATE"
    TRAVEL_DAYS = "TRAVEL_DAYS"
    EVENT_DAYS = "EVENT_DAYS"
    SUBMIT = "SUBMIT"

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
        [sg.CalendarButton(button_text="Start Date", target=Key.START_DATE.value, format="%y-%m-%d"),sg.In(key=Key.START_DATE.value,enable_events=True,visible=True,size=(20,1))],
        [sg.Text("Travel Days:"),sg.InputText(key=Key.TRAVEL_DAYS.value,size=(2,1)),sg.Text("Event Days:"),sg.InputText(key=Key.EVENT_DAYS.value,size=(2,1))],
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
    folders.append(Key.TROPHY.value),

if values[Key.CERTIFICATES.value]:
    folders.append(Key.CERTIFICATES.value)

for k, v in values.items():
    print(f"{k}: {v}")

# for each_folder in folders:
#     print(f"Now adding {each_folder} into path")
#     new_folder_path = os.path.join(values["PATH"],each_folder)
#     print(new_folder_path)
#     os.mkdir(new_folder_path)




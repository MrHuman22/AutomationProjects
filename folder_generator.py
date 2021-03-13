"""
Every event requires me to make x number of folders.
Extract file path from choose a folder using the PySimpleGUI browser and make a list of folders inside
Some Optional Folders

Folders:
/Event/
    - PRFs
    - Score Sheets
    - Accommodation
    - Guides
    - Attendance Sheets
    - Certificates
    - Travel Diary
    - Flights (Optional)
    - Trophy (Optional)
"""

import PySimpleGUI as sg
import os
from enum import Enum

class Key(Enum):
    PATH = "PATH"
    TROPHY = "TROPHY"
    FLIGHTS = "FLIGHTS"

folders = [
    "PRFs",
    "Score Sheets",
    "Guides",
    "Attendance Sheets",
    "Certificates",
    "Travel Diary",
    "Final Report"
]

layout = [[sg.Text("Choose an event folder"),sg.FolderBrowse(key=Key.PATH.value)],
        [sg.Checkbox("Flights?",key=Key.FLIGHTS.value)],[sg.Checkbox("Trophy?",key=Key.TROPHY.value)],
        [sg.Submit()]]

window = sg.Window("Generate Event Folders", layout)

event, values = window.read()
window.close()

if values["FLIGHTS"]:
    folders.append("Flights"),

if values["TROPHY"]:
    folders.append("Trophy")

for each_folder in folders:
    print(f"Now adding {each_folder} into path")
    new_folder_path = os.path.join(values["PATH"],each_folder)
    print(new_folder_path)
    os.mkdir(new_folder_path)




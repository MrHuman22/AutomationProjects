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

Automatically adds event day subfolders to the PRFs folder

Stretch Goal:
TODO:
Also generates a packing list in my private Trello
"""

import PySimpleGUI as sg
import os
import shutil
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
    TO_PRINT = "To Print"
    MEDIA_CONSENT = "Media Consent"
    QR_CODES = "QR Codes"
    CHALLENGE_DAY = "Challenge Day"
    DISCOVERY_DAY = "Discovery Day"
    EVENT_NAME = "Event Name"
    DD_TGUIDE_FILENAME = "TEACHERS GUIDE Discovery Day Mail Merge"
    CD_TGUIDE_FILENAME = "TEACHERS GUIDE Challenge Day Mail Merge"
    DD_EGUIDE_FILENAME = "EVENT GUIDE Discovery Day Mail Merge"
    CD_TGUIDE_FILENAME = "EVENT GUIDE Challenge Day Mail Merge"



class Event():
    def __init__(self):
        self.api_key = config(Key.TRELLO_API_KEY.value)
        self.token = config(Key.TRELLO_TOKEN.value)
        self.date_format = "%y-%m-%d"
        self.folders = [
            "PRFs",
            "Score Sheets",
            "Guides",
            "Attendance Sheets",
            "Certificates",
            "Travel Diary",
            "Final Report"]

    def get_info(self):
        
        layout = [
                [sg.Text("Event Name: "),sg.InputText('',key=Key.EVENT_NAME.value)],
                [sg.Text("Choose an event folder:"),sg.FolderBrowse(key=Key.PATH.value)],
                [sg.CalendarButton(button_text="Travel Start Date", target=Key.START_DATE.value, format=self.date_format),sg.In(key=Key.START_DATE.value,enable_events=True,visible=True,size=(20,1))],
                [sg.Text("Travel Days before:"),sg.InputText(key=Key.TRAVEL_DAYS_BEFORE.value,size=(2,1)),sg.Text("Event Days:"),sg.InputText(key=Key.EVENT_DAYS.value,size=(2,1)),sg.Text("Travel Days After:"),sg.InputText(key=Key.TRAVEL_DAYS_AFTER.value,size=(2,1))],
                [sg.Checkbox("Challenge Day?", key=Key.CHALLENGE_DAY.value), sg.Checkbox("Event Day?", key=Key.CHALLENGE_DAY.value)],
                [sg.Checkbox("Trophy?",key=Key.TROPHY.value), sg.Checkbox("Certificates?",key=Key.CERTIFICATES.value)],
                [sg.Submit(key=Key.SUBMIT.value)]]

        window = sg.Window("Generate Event Folders", layout)

        while True:
            self.event, self.values = window.read()
            print(f"event: {self.event},values: {self.values}")
            if self.event == "Exit" or self.event == Key.SUBMIT.value or self.event== sg.WIN_CLOSED:
                window.close()
                break

        
    def add_folders(self):
        if self.values[Key.TROPHY.value]:
            self.folders.append(Key.TROPHY.value.title()),

        if self.values[Key.CERTIFICATES.value]:
            self.folders.append(Key.CERTIFICATES.value.title())

        for k, v in self.values.items():
            print(f"{k}: {v}")

        for each_folder in self.folders:
            print(f"Now adding {each_folder} into path")
            new_folder_path = os.path.join(self.values[Key.PATH.value],each_folder)
            print(new_folder_path)
            if not os.path.exists(new_folder_path):
                os.mkdir(new_folder_path)
            else:
                pass

    def add_subfolders(self):
        # now adding the subfolders for each day in the PRF folder and To Print
        # find the actual start date by taking the travel start date and adding travel_days_before
        travel_start_date = datetime.strptime(self.values[Key.START_DATE.value],self.date_format)
        event_start_date = travel_start_date + timedelta(days=int(self.values[Key.TRAVEL_DAYS_BEFORE.value]))
        event_day_count = int(self.values[Key.EVENT_DAYS.value])
        for x in range(event_day_count):
            event_date = event_start_date + timedelta(days=x)
            folder_name = event_date.strftime(self.date_format + " %a")
            # print(folder_name)
            # Add subfolders to PRFs
            prf_subfolder_path = os.path.join(self.values[Key.PATH.value],Key.PRFS.value,folder_name)
            os.mkdir(prf_subfolder_path)
            # Add subfolders to media consent
            # media_consent_subfolder_path = os.path.join(self.values[Key.PATH.value],Key.MEDIA_CONSENT.value,folder_name)
            # os.mkdir(media_consent_subfolder_path)
            # toprint_subfolder_path = os.path.join(self.values[Key.PATH.value], Key.TO_PRINT.value,folder_name)
            # os.mkdir(toprint_subfolder_path)

    def copyfiles(self):
        # Now copy over the event and challenge guides
        event_guide_template_path = r"C:\Users\pwn394\The University of Newcastle\SEC - SEC\EVENTS\Management\Event and Teacher Guide Mail Merge Templates"
        if self.values[Key.CHALLENGE_DAY.value]:
            event_guide_path = os.path.join(event_guide_template_path,Key.CD_TGUIDE_FILENAME.value)
            print(f"Event Guide Path: {event_guide_path}")
            # Teacher's Guide
            new_event_guide_path = os.path.join(Key.PATH.value,Key.CD_TGUIDE_FILENAME.value)
            print(f"new_event_guide_path: {new_event_guide_path}")

            # copy the file over
            # shutil.copy(event_guide_path,new_event_guide_path}")
            
            new_event_guide_filename = os.path.join(Key.PATH.value,"Guides",f"{self.values[Key.EVENT_NAME.value]} Challenge 2021 Teacher's Guide")
            print(f"new_event_guide_filename: {new_event_guide_filename}")
            # os.rename(os.path.join(Key.PATH.value,"Guides",Key.CD_TGUIDE_FILENAME),os.path.join(Key.PATH.value,"Guides",f"{self.values[Key.EVENT_NAME.value]} Challenge 2021 Teacher's Guide"))


    def add_to_trello(self):
        pass
        # Copy and rename the path


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

def main():
    e = Event()
    e.copyfiles()

if __name__ == "__main__":
    main()
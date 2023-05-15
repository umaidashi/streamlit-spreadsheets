import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import time


def spreadsheets():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        'client_secret.json', scope)
    client = gspread.authorize(creds)

    sheet = client.open("test").sheet1

    list_of_hashes = sheet.get_all_records()
    print(list_of_hashes)
    return list_of_hashes


scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(
    'client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open("").sheet1

all_records = sheet.get_all_records()

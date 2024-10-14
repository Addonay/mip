import json
import csv
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SPREADSHEET_ID = "1bazcKli9Bfo-nQJJSEx8h-7LWxprDKPhVki9LpW67yY"

def main():
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("creds.json", SCOPES)
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("sheets", "v4", credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range="Sheet1").execute()
        values = result.get("values", [])

        if not values:
            print("No data found.")
        else:
            print("Name, Major:")
            for row in values:
                # Print columns A and E, which correspond to indices 0 and 4.
                print(f"{row[0]}, {row[4]}")

    except HttpError as error:
        print(f"An error occurred: {error}")
        values = None


if __name__ == "__main__":
    main()


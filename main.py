from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive']

#Dictonary of the classes
Classes = {
     1:{
            #Name of you class
            "Class": "Math",
            #the google docs id of your pre-created documnet
            "GoogleDocsID": "Insert here the ID of the pre-created mla documnet"
        },
     2: {
            "Class": "Bio",
            "GoogleDocsID": "Insert here the ID of the pre-created mla documnet"
        },
     3:  {
            "Class": "Phy",
            "GoogleDocsID": "Insert here the ID of the pre-created mla documnet"
        },
     4: {
            "Class": "Art",
            "GoogleDocsID": "Insert here the ID of the pre-created mla documnet"
        }
}

def main():
    #Used to ask the user what class is the document for and get the ID for the class
    title, fileID = UserInput()
    
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    #Using the version 3 of the drive
    service = build('drive', 'v3', credentials=creds)


    #body of the new copy title
    body = {
        'name': title,
        
    }
    
    drive_response = service.files().copy(fileId=fileID, body=body).execute()
    document_copy_id = drive_response.get('id')


#Used to see what class is the user creating the documnet for
def UserInput():
    #Displays all the classes availible 
    for item in Classes:
        print(str(item)+ ':', Classes[item]['Class'])
    Class = input("What class is this for (Please Enter the Number)?")
    title = input("What is the name of your new documnet?")
    #Gets the Google ID for the class
    GoogleID = Classes[int(Class)]['GoogleDocsID']
    
    return title, GoogleID


if __name__ == '__main__':
    main()

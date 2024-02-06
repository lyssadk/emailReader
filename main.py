import os.path
import re
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import base64 
from bs4 import BeautifulSoup

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def main():
  """Shows basic usage of the Gmail API.
  Lists the user's Gmail labels.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

  try:
    # Call the Gmail API
    service = build("gmail", "v1", credentials=creds)

     # request a list of all the messages  
    result = service.users().messages().list(maxResults=2, userId='me').execute() 
    messages = result.get('messages') 
    discounts = []
    items = []
    for msg in messages: 
        # Get the message from its id 
        txt = service.users().messages().get(userId='me', id=msg['id']).execute() 
        payload = txt['payload']
        
        parts = payload.get('parts')
        if parts is not None:
          data = parts[0]['body']['data']
        else:
          print("Parts is None")
          continue

        data = data.replace("-","+").replace("_","/") 
        decoded_data = base64.b64decode(data) 
        soup = BeautifulSoup(decoded_data , "lxml") 
        body = str(soup.findAll('p'))
        keyWord = "Order summary"
        # res=str(body)[str(body).find(keyWord)+len(keyWord):]
        orderSummary = body[str(body).find(keyWord)+len(keyWord):str(body).find("Customer information")]
        print(orderSummary)
        if orderSummary.find("Discount"):
          discount = orderSummary[orderSummary.find("Discount")+len("Discount"):orderSummary.find("Subtotal")]
          discounts.append(discount)
          itemList = str(body)[str(body).find(keyWord)+len(keyWord):str(body).find("Discount")]
          print(itemList)
        else:
          print("No discount")
          itemList = str(body)[str(body).find(keyWord)+len(keyWord):str(body).find("Subtotal")]
          print(itemList)
        # if discount -> pull the discount and save it into a variable
        # else - > go straight to subtotal
       


        #\:1gv > div:nth-child(1) > div > div:nth-child(1) > div:nth-child(5) > table > tbody > tr > td > table:nth-child(3) > tbody > tr > td > center > table:nth-child(2) > tbody > tr > td > table:nth-child(1) > tbody > tr:nth-child(1) > td > table > tbody > tr > td:nth-child(2)
          
        # Use try-except to avoid any Errors 

  except HttpError as error:
    # TODO(developer) - Handle errors from gmail API.
    print(f"An error occurred: {error}")

if __name__ == "__main__":
  main()
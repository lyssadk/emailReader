import os.path
from dotenv import load_dotenv
import pymongo
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import base64 
from bs4 import BeautifulSoup

load_dotenv()
# Scopes
# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

# database connection 
myclient = pymongo.MongoClient(os.getenv('MONGO_URI'))
# print(myclient.list_database_names())
# ordersCollection = myclient["Orders"]
# itemsCollection = myclient["Items"]


def main():
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
    result = service.users().messages().list(maxResults=1, userId='me').execute() 
    messages = result.get('messages') 
    for msg in messages: 
        # Get the message from its id 
        txt = service.users().messages().get(userId='me', id=msg['id']).execute()

        # get the payload from the email message
        payload = txt['payload']
        parts = payload.get('parts', [])
        data = parts[0]['parts'][0]['body']['data']
        # get the headers from the payload | this returns a list of headers to loop through
        headers = payload['headers']

        # loop through the headers and get the Subject aka the order number which will be the ID
        for header in headers:
          if header['name'] == 'Subject':
            subject = header['value']
            orderNumber = subject[subject.find("Order")+len("Order "): subject.find("confirmed")]
            print(orderNumber)
        

        data = data.replace("-","+").replace("_","/") 
        decoded_data = base64.b64decode(data) 
        soup = BeautifulSoup(decoded_data , "lxml") 
        text = str(soup.body()) 
        keyWord = "Order summary"
        # res=text[text.find(keyWord)+len(keyWord):]
        # find the order summary
        orderSummary = text[text.find(keyWord)+len(keyWord):text.find("Customer information")]

        # if the order summary has a discount
        # if discount -> pull the discount and save it into a variable
        # else - > go straight to subtotal
        if orderSummary.find("Discount"):
          # get the discount and save it into a variable
              discount = orderSummary[orderSummary.find("Discount")+len("Discount"):orderSummary.find("Subtotal")]
              print(discount)

          # get the items and save  them into a variable
              itemList = text[text.find(keyWord)+len(keyWord):text.find("Discount")]
              print(itemList)
        else:
              print("No discount")
          # get the items and save them into a variable
        
        itemList = text[text.find(keyWord)+len(keyWord):text.find("Subtotal")]

          #get the information to insert into the order database
        total = text[text.find("Total")+len("Total"):text.find("Customer information")]
        subtotal = text[text.find("Subtotal")+len("Subtotal"):text.find("Shipping")]  
        shipping = text[text.find("Shipping")+len("Shipping"):text.find("Total")]
          # data = parts['body']['data']
        print("Total: ", total, "Subtotal: ", subtotal, "Shipping: ", shipping)
        # get the data from the body of the email

  
        
        # decode the data
        
        
        # if ordersCollection.
        #   ordersCollection.insert_one({"OrderNumber": orderNumber, "Total": total, "Subtotal": subtotal, "Shipping": shipping})
        # else:
        #   print("Order already exists")
          #myDict = {"Total": total, "Subtotal": subtotal, "Shipping": shipping}
          #print(myDict)
          

        
      

  except HttpError as error:
    # TODO(developer) - Handle errors from gmail API.
    print(f"An error occurred: {error}")

if __name__ == "__main__":
  main()
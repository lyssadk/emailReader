# Overview
My mom owns a business and she recieves inventory from various companies. They send her the reciepts to her email and at the end of the year when she is prepping for taxes and getting organized, it takes a very long time. My goal is to use the Gmail RESTful API to pull the messages and parse through them to get the information she needs and put them into a MongoDB database. 

Ideally it will be able to take multiple emails, and then calculate different totals, tell her based on her sales, how many she should have in inventory. IT should also be able to simplify all the information needed to complete her taxes. When her company grows i would also like to have it track the most commonly bought items, what months are the highest buying, etc. 

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the data set, the questions and answers, the code running and a walkthrough of the code.}

[Software Demo Video](http://youtube.link.goes.here)

# Data Analysis Results
Currently working on issues of parsing through the emails, for plain text emails i've been able to get the information i need. However for the recent reciepts i've been looking at, the format is different as it has some images that is causing my code to have a stroke. It works randomly, but trying to do some error handling to guarantee it every time.

# Development Environment
pip3 -- i tried using pip with python3 and soon discovered that my computer didn't appreciate that:)
python3
Beautiful Soup
Gmail RESTful api
lxml
MongoDB
Visual Studio Code
Google Cloud project
email

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [SigParser Guide](https://sigparser.com/developers/email-parsing/gmail-api/)
* [Gmail RESTful API](https://developers.google.com/gmail/api/guides)
* [Geek For Geeks guide](https://www.geeksforgeeks.org/how-to-read-emails-from-gmail-using-gmail-api-in-python/)
* [Beautiful Soup Docs](https://beautiful-soup-4.readthedocs.io/en/latest/)

# Future Work
* connect to mongoDB and update it with what is pulled from each email
* get consistent results from the Gmail API
* in the meantime so my mom can still automate it, just copy and paste the info from emails to test the database

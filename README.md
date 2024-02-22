# Overview
My mom owns a business and she recieves inventory from various companies. They send her the reciepts to her email and at the end of the year when she is prepping for taxes and getting organized, it takes a very long time. My goal is to use the Gmail RESTful API to pull the messages and parse through them to get the information she needs and put them into a MongoDB database. 

Ideally it will be able to take multiple emails, and then calculate different totals, tell her based on her sales, how many she should have in inventory. IT should also be able to simplify all the information needed to complete her taxes. When her company grows i would also like to have it track the most commonly bought items, what months are the highest buying, etc. 

Link to video demonstration coming soon!

# Data Analysis Results
Currently working on issues of parsing through the emails with reciepts that have slightly different things (some have state taxes, discounts, etc) so i will need to finish those logic statements, then i should be able to get the data analysis desired.

# Development Environment
* pip3
* python3
* Beautiful Soup
* Gmail RESTful api
* lxml
* MongoDB
* Visual Studio Code
* Google Cloud project
* email

# Useful Websites
* [SigParser Guide](https://sigparser.com/developers/email-parsing/gmail-api/)
* [Gmail RESTful API documentation](https://developers.google.com/gmail/api/guides)
* [Geek For Geeks guide](https://www.geeksforgeeks.org/how-to-read-emails-from-gmail-using-gmail-api-in-python/)
* [Beautiful Soup Docs](https://beautiful-soup-4.readthedocs.io/en/latest/)

# Future Work
* connect to mongoDB and update it with what is pulled from each email
* clean up code into functions, clearer comments
* add some if statements for the slight variations of the emails

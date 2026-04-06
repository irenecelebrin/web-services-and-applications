# Slackline Ireland web application: design  

## Concept 

Goal: Manage Slackline Ireland memberships. 
The application will allow admins to manage memberships and membership requests. 
Some members pay a contribution, others don't. 
Optional: the application will allow new members to register. the application will need to be reviewed by an admin, before being added to the database. 

## Components 

- A relational database (in theory, with MySQL, but it might be SqlLite, if easier to manage) 
- Backned using Flask 
- A Front End. this will be the last step 
- eventually the code will be hosted in python


## Properties: 
    id
    name
    surname
    phone number 
    email
    DOB
    Emergency contact (dict: name: xx, surname: xx)
    Date enrolled
    Last contribution date
    Contribution paid


## Functionalities 

ADD NEW MEBER 
required: 
    name
    surname
    phone number 
    email
    DOB
    emergency contact

There can be a form to add a new member as registration, pending admin review --> send automated emails. 

READ ALL 
2 views: 
    - for admins 
    See all details 
    - for members 
    See only 


READ BY ID or SURNAME

UPDATE
    - by id 

DELETE 

## Database 

Relational database, initially imported from a csv file 

## Backup 

Every time a change is made, a backup is created and stored on the cloud (where?). 
It would be ideal to update the exsitng google spreadsheet file. 

## Hosting 

Python anywhere 


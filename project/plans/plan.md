# Slackline Ireland web application: design  

## Concept 

Goal: Manage Slackline Ireland memberships. See db.csv
The application will allow admins to manage memberships and membership requests. 
Some members pay a contribution, others don't. 
Optional: the application will allow new members to register. The application will need to be reviewed by an admin, before being added to the database. 

## Components 

1. A relational database (in theory, with MySQL, but it might be SqlLite, if easier to manage). the db will be created importing a csv file (see db.csv)
2. Backend using Flask. There will be a server.py with the Flask application. Also, there will be a person_DAO.py defining the functions to perform CRUD operations. 
3. A Front End so users can perform CRUD operations. This will be the last step. 
4. Eventually the code will be hosted in pythonanywhere or another hosting service. 


## 1. Database 

Relational database, initially imported from a csv file. Import existing data from the csv file db.csv, but also add other fields.  

Information in the file: 
Date registered
Name
Last Name
Email
Phone number
Address
Emergency Contact Name
Emergency Contact Phone Number
Date of Birth (dd/mm/yy)

### Database schema

**People**
ID -- auto increment, number, primary key, foreign key linking to Membership
Name --varchar
Last Name -- varchar
Email --varchar
Phone Number -- number
Address --varchar
Emergency Contact ID --number, autoincrement, foreign key linking to Emergency contactsa 

**Emergency contacts**
Emergency contact ID -- number, primary key
Emergency contact name -- varchar
Emergency contact phone number -- number 

**Memberships**
ID --numer, primary key 
Registration Date -- date
Membership payment date -- date
Membership payment (€) -- number 

##2. Backend: CRUD Functionalities 

VIEW ALL MEMBER 
- view all members and related information --> this is for admins 

- optional: view only your information (this is only for members) and current membership information and Emergency contacts

ADD NEW MEBER 
required: 
    name
    surname
    phone number 
    email
    emergency contact name 
    emergency contact number 
    Membership payment (€) can be null 

Once a new member is added, also information on registration date will be stored as "Registration date" and if a membership is paid, the membership date will be added. 

READ BY ID or SURNAME

Search for a member by surname, email address, or id number (which is probably not useful)

UPDATE

Update any field:
Membership payment --> this will also save a new Membership date (current date)
email
phone number 
name
surname
emergency contact name
emergency contact number

DELETE 

Delete a member 

### Backup 
Every time a change is made, a backup is created and stored on the cloud (where?). 
It would be ideal to update the exsitng google spreadsheet file. 

## 3. Front End
Create front end using Javascript, html and css. TBD at a later stage

## 4. Hosting 
Python anywhere, or other service 


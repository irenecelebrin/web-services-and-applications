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
Date of birth
Emergency Contact ID --number, autoincrement, foreign key linking to Emergency contacts 

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

## Appendix

Database choice

Do you think it's better to use SQL Lite or MySQL, if I want my code to be hosted and to last? I don't plan on having loads of data in the database, at any time 

Good question. For your use case, SQLite is the better choice. Here's why:

SQLite advantages for this project:

Hosting simplicity -- PythonAnywhere (which you mentioned) supports SQLite out of the box with zero setup. MySQL on PythonAnywhere requires a paid plan, while SQLite works on the free tier.
No server process -- SQLite is just a file (slackline.db). No database server to configure, maintain, or worry about crashing. This is a big win for a small app you want to "just work" long-term.
Backup is trivial -- you can back up the entire database by copying a single file.
More than enough capacity -- SQLite comfortably handles databases up to ~280 TB. With a membership list of dozens (or even thousands) of people, you'll never come close to its limits.
Zero extra dependencies -- sqlite3 is built into Python's standard library.
When would MySQL be worth it instead?

Multiple concurrent writers (e.g., hundreds of users submitting forms simultaneously) -- not your case
Multiple separate applications need to share the same database -- not your case
You need fine-grained user permissions on the database itself -- not your case
The one thing to be aware of: if you ever did need to migrate to MySQL later, the switch would be straightforward since the DAO layer abstracts all the SQL. You'd only need to change person_dao.py (swap sqlite3 for mysql.connector and adjust a few query syntax details). The rest of your code stays the same.

For a small membership app on PythonAnywhere that you want to last with minimal maintenance, SQLite is the pragmatic choice. Ready to start building when you are.
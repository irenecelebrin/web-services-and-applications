# Web services and Applications: Final project 

Final project for the course "Web services and applications", Higher Diploma in Computing for Data Analytics, ATU Galway Mayo, 2026. 

The project is a REST API created for the admins of the sports association Slackline Ireland to manage member registrations, subscriptions and emergency contacts. 

## Getting started 

The API connects a relational database to a Front End in Javascript. The programming languages used are: 

- SQL (the database)
- Python (for back end)
- Javascript, CSS, HTML (for the front end)

To install the required dependencies: 

> pip install -r requirements.txt 

## The project: Slackline Ireland memberships 

In my daily worklife I have access and use LLMs and AI agents extensively. However, for security reasons, it wasn't possible for me to use any of my work projects for this course. So I decided to take inspiratipn from  my hobbies and created a database to manage the members of the Slackline community in Dublin. 

What is slackline? Basically, it's about walking on a loose rope (or slack): you can do it in the park, in the forest, in the mountains. 
Slackline Ireland is a small but mighty group of people. It's an informal, self-regulated organization. We regularly meet up in the park, go on adventures around Ireland, share knowledge and best practices, and above all have fun wiggling above the ground. 

Joining the group and being a member is free, but we want to keep track of regular attendees, know about their emergency contact, and track if they want to join our winter indoor sessions (and in that case, track payments). It just made sense to move on from out regular Excel sheet and create our own (small but mighty) application.

## The implementation 

### 1. Database 

**Database creation**  

The database is created parsing the data from the existing csv [db_anonymised.csv](project/data/db_anonymised.csv) and iporting it into a relational database using SQLite: [slackline.db](data/slackline.db) The real data from the Slackline Ireland was anonymised to respect the privacy of its members. 
The script used to parse the dtaa is [import_data.py](import_data.py). 

**Database structure**

The database is created using the script [create_database.py](create_database.py). The program defines 3 tables: 
- People: the main table with the list of members, contacts and addresses. It includes 1 foreign key linking to the table *emergency contacts*. 

<img src="data/schema_people.png" alt="People schema" width="600">

- Emergency contacts it includes name and numbers of emergency contacts for every member.  

<img src="data/schema_contacts.png" alt="Emergency contacts" width="600">

- Memberships: this table includes data like registration dates and payments (note: paying a contribution is not required, any member can choose to do it to fund the organization and access extra activities).

<img src="data/schema_memberships.png" alt="Memberships" width="600">

How to use SQLite: [sqllite.org](https://sqlite.org/), [sqlite3 on python](https://docs.python.org/3/library/sqlite3.html)


### 2. Backend

####**Flask app** 

In [server.py](server.py), a Flask app is created to set up an API allowing CRUD functionalities to the database [slackline.db](data/slackline.db). 

The functionalities are the following: 

CREATE: 

- **Add a new member**: Route: /api/persons. Fields required: name, last_name, phone, email, emergency_contact_name, emergency_contact_phone in the JSON body

READ: 

- **View all members**. Route: /api/persons. It returns all members. Info? 

- **Find member by id**. Route: /api/persons/<id>. Returns a single member by id.

- **Find member by surname**. Route: /api/persons/surname/<value>. Searches members by surname (case-insensitive) -- easier to use in real life. 

- **Find member ny email**. Route: /api/persons/email/<value>. Searches members by email (case-insensitive).

UPDATE: 

- **Update member details**. Route: /api/persons/<id>. Partially updates a member by ID. Returns 404 if not found.

DELETE: 

- **Delete members**. Route: /api/persons/<id>. Deletes a member by ID. It deletes all information related to that memeber ID (not on cascade, but in the person DAO). Returns 404 if not found, or {"deleted": id} on success.


####**Person DAO** 

### 3. Front End 


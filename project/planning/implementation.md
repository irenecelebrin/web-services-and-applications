# Slackline Ireland memberships 

## About this project 

In my daily worklife I have access and use LLMs and AI agents extensively. I work on AI applications for consumer products, so I use AI improve the prompts of AI applications, test improvements and regressions, automate internal workflows, understand what complex internal code does. However, for security reasons, it wasn't possible for me to use any of my work projects for this course. So I decided to use my hobbies. 

### The use case 
I decided to create a databse to manage the members of the informal sports association Slackline Ireland. 

What is slackline? Basically, it's about walking on a loose rope (or slack): you can do it in the park, in the forest, in the mountains. 

Slackline Ireland is a small but mighty group of people. It's an informal, self-regulated organization. We regularly meet up in the park, go on adventures around Ireland, share knowledge and best practices, and above all have fun wiggling above the ground. 

Joining the group and being a member is free, but we want to keep track of regular attendees, know about their emergency contact, and track if they want to join our winter indoor sessions (and in that case, track payments). 
I suggested to move on from the regular Excel sheet we use to manage members, and create our own (small but mighty) application. 

## Back end 
###  1. Database creation

A database is created using SqLite. 
The data is parsed from the csv and added to the tables in the database: 

People [add schema]

Emergency contacts [add schema]

Memberships [add schema]

## Import existing csv data 

The data is imported and added to the 3 tables 

### 2. Server.py

The crud functionalities are added to server.py

Imports the full DAO surface.
GET /persons → get_all().
GET /persons/<int:id> → get_by_id(), 404 if missing.
New GET /persons/surname/<value> and GET /persons/email/<value> (return [] on no match, not 404).
POST /persons → validates name, last_name, phone, email, emergency_contact_name, emergency_contact_phone; 400 lists which are missing; otherwise create() and returns 201 with the new member.
PUT /persons/<int:id> → calls update(), 404 if missing, else returns the updated member.
DELETE /persons/<int:id> → calls delete(), 404 if missing, else 204.
Note on payload field name: the create route uses last_name (matching the DB column and CSV import), even though the plan informally said "surname". If you'd rather accept surname from clients, I can add an alias.


### 3. Person DAO 

project/person_dao.py — full SQLite implementation
- _connect() opens slackline.db (resolved next to the file), enables PRAGMA foreign_keys = ON, and sets sqlite3.Row for dict-friendly rows.

- _MEMBER_SELECT_SQL is the shared JOIN across people, emergency_contacts, and memberships so all reads return the same flat shape.

- Reads: get_all(), get_by_id(id), get_by_surname(value), get_by_email(value) — surname/email use case-insensitive exact match.

- create(person) — within a single transaction inserts emergency contact → person → membership; stamps registration_date = today, and if payment_amount is provided, also stamps payment_date = today. Returns the created member.

- update(id, person) — partial update; builds dynamic UPDATE per table only for keys present in the payload. If payment_amount is in the payload, also stamps payment_date = today (per plan §2). Returns None if id missing.

- delete(id) — cascade as you chose: deletes the memberships row, then people row, then the linked emergency_contacts row. Returns False if id missing.


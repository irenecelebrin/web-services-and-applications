# Web services and Applications: Final project 

Final project for the course "Web services and applications", Higher Diploma in Computing for Data Analytics, ATU Galway Mayo, 2026. 

The project is a REST API created for the admins of the sports association Slackline Ireland to manage member registrations, subscriptions and emergency contacts. 

## The project: Slackline Ireland memberships 

In my daily worklife I have access and use LLMs and AI agents extensively. However, for security reasons, it wasn't possible for me to use any of my work projects for this course. So I decided to take inspiratipn from  my hobbies and created a database to manage the members of the Slackline community in Dublin. 

What is slackline? Basically, it's about walking on a loose rope (or slack): you can do it in the park, in the forest, in the mountains. 
Slackline Ireland is a small but mighty group of people. It's an informal, self-regulated organization. We regularly meet up in the park, go on adventures around Ireland, share knowledge and best practices, and above all have fun wiggling above the ground. 

Joining the group and being a member is free, but we want to keep track of regular attendees, know about their emergency contact, and track if they want to join our winter indoor sessions (and in that case, track payments). It just made sense to move on from out regular Excel sheet and create our own (small but mighty) application.

**So what's the use case?** 

Thi project is a REST API created for the admins of the sports association Slackline Ireland to manage member registrations, subscriptions and emergency contacts. 

## Getting started 

### Dependencies

The API connects a relational database to a Front End in Javascript. The programming languages used are: 

- SQL (the database)
- Python (for back end)
- Javascript, CSS, HTML (for the front end)

To install the required dependencies: 

    pip install -r requirements.txt 

### Running the application locally 

Start the Flask app: 

    python server.py

To perform CRUD operations using the UI, open this url with your browser:

    http://127.0.0.1:5000

To make curl requests from your terminal,  use the routes described in section **2. Backend / Flask app**, adding to the Headers the parameter *Accept: application/json*.  For example, to view a member by id: 

    curl -H "Accept: application/json" http://localhost:5000/person/1

Or to create a new member: 

    curl -X POST http://localhost:5000/form \
    -H "Content-Type: application/json" \
    -d '{
        "name": "John",
        "last_name": "Doe",
        "phone": "0712345678",
        "email": "john.doe@example.com",
        "emergency_contact_name": "Jane Doe",
        "emergency_contact_phone": "0787654321"
    }'

For more information on curl requests, visit [curl.se](https://curl.se/docs/httpscripting.html) or type the command: 

    curl --help

### Hosted version  


la-dee-da 


## The implementation 

### 1. Database 

**Database creation**  

The database is created parsing the data from the existing csv [db_anonymised.csv](project/data/db_anonymised.csv) and iporting it into a relational database using SQLite: [slackline.db](data/slackline.db). The real data from the Slackline Ireland was anonymised to respect the privacy of its members. 

*Why SQLite*: it was chosen because the amount of data to handle was not signifiant, and for its portability (no installation required, ready-to-use in all operating systems, once python is installed). 

The script used to parse the data is [import_data.py](import_data.py). 

**Database structure**

The database is created using the script [create_database.py](create_database.py). The program defines 3 tables: 
- People: the main table with the list of members, contacts and addresses. It includes 1 foreign key linking to the table *emergency contacts*. 

<img src="data/schema_people.png" alt="People schema" width="600">

- Emergency contacts it includes name and numbers of emergency contacts for every member.  

<img src="data/schema_contacts.png" alt="Emergency contacts" width="600">

- Memberships: this table includes data like registration dates and payments (note: paying a contribution is not required, any member can choose to do it to fund the organization and access extra activities).

<img src="data/schema_memberships.png" alt="Memberships" width="600">

How to use SQLite: [sqllite.org](https://sqlite.org/), [sqlite3 on python](https://docs.python.org/3/library/sqlite3.html)


### 2. Flask app and Person DAO

In [server.py](server.py), a Flask app is created to serve both the HTML front end and a JSON API, allowing CRUD functionalities on the database [slackline.db](data/slackline.db).

Each route serves two purposes in delivering content: browser requests receive the corresponding HTML page, while requests with the `Accept: application/json` header receive JSON data. This means there are no separate `/api/` paths — the same URL serves both the UI and the API. This means that the requests can be made from terminal (to get Json responses) or from the web UI (for users). 
This was achieved after some prompt iteration to avoid a huge number of routes. 

| Route | Methods | Description |
|---|---|---|
| `/persons` | GET | Members list page / JSON list of all members |
| `/persons/surname/<value>` | GET | Members list filtered by surname (case-insensitive) |
| `/persons/email/<value>` | GET | Members list filtered by email (case-insensitive) |
| `/person/<id>` | GET | Member detail page / JSON for a single member |
| `/person/<id>` | PUT | Partially update a member by ID (JSON body) |
| `/person/<id>` | DELETE | Delete a member by ID |
| `/form` | GET | Add / edit member page |
| `/form` | POST | Create a new member (JSON body); returns 201 on success |

**Required fields for creation (POST /form):** `name`, `last_name`, `phone`, `email`, `emergency_contact_name`, `emergency_contact_phone`.

All write operations return 404 if the member is not found. DELETE returns `{"deleted": id}` on success.

EXTRA: There are two static routes for the landing page and the gallery of the web UI: 

| Route | Description |
|---|---|
| `/` | Index |
| `/gallery/<path:filename>` | Send to gallery |


The **person DAO** includes the functions to connect to the database and perform the CRUD operations mapped in the Flask APP. 


### 3. Front End 


## AI usage 

This project was created with extensive use of AI. The AI Agent used was Claude-4.6-sonnet, through [Cursor](https://cursor.com/). Cursor is an IDE that allows to integrate AI assistants in your workflow. For this reason, I was not able to produce any links as reference. 

However, this is how the project was implemented: 

- The SQL lite database was designed and implemented by me.
- I created the Flask app and the person DAO to support json reponses (no web UI). 

Ai helped with: 

- Modifying the Flask App and the person DAO to support the double function of json responses / web application. 
- Creating the Front End from scratch. 

This still required extensive prompting to follow the design I had in mind and avoid unnecessary redundiancies. For example, AI first created new routes from scratch and linked them to static html templates for the web application, before I asked to have the same routes with both functionalities. 



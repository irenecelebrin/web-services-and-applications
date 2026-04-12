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
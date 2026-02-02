Date: 02-02-2026 
author: irene celebrin 


# 0 Introduction 
## 0.1 HTML and Javascript 

resources: W3school

HTML: markup language, used for the web 
Javasccript: dynamic language, adds dynamic actions to HTML. Learnmore on W3school. 

Create a file with HTML and Js and open the code with a browser to display the output. If you open developer tools, you can see the console and what is going on in the background (logs, debugging...). 
Javascript can be embedded in HTML witht he script tags 

Good Js tutorial on W3school 

## 0.2 WAMP

Install database on your machine --> WAMP 

Mac: look at what gerard is doing for applied databases. 

WAMP: Windows, Apache, MySQL, PHP. 

MySQL is ok but using a proper database is better. 

MySqlbench (no password) to use mySQL 

PhMyAdmin: to crete a new database, tables etc. 

once you install wamp 64, you can open html pages with: 
- webserver: with localhost/...
- file directories c:users/irene/... --> which will not work for other users on their machines. 


# 1. Representing data 

## 1.1 json and xml 

in sofware: 
- variables, lists, dicts, arrays...
- picke

as a table
- excel
- sql database
- csv file 

ad a text file:
- simple text
- json
- xml 

lots of others: 
- charts 

Any way we store data can alter the way of reading and working with the data 

Things to consider when deciding on data format: 
- is it human readable? 
- how is the data organised? 
- ease of modification
- efficiency of space
- robustness 

--> xml and json are human readable, simple, compact, nested, standardised. 

Example of APIs: irishrail with real time tracker (xml format)

tags are used for attributes (train code, status...)

for a list of APis, check 

## 1.2 Types of relationships 

- embed everything: everything is in one table. Good for 1 to 1 relationship 
- Foreign key: for dealing with 1 to many or many to many relationships 

## xml 

extensible markup language
create to create rich format text 

there is a root tag 
and the elememts. 
elements have an open and close tag. 

html tags are predefined, xml not
xml was defined to carry/represent data 
html was designed for browser display 

xml information is to display information in text format 
xml does not do anything (like html)
there are no predefined tags 
xml has a tree-like syntax
the documentt object model (DOM) can be applied to xml 


elements: 
declaration 
root element
elements 
tags 
attributes 

Ways to parse through XML data: 
-  SAX: simple API for XML 
- DOM: document object module 
    - reads in the whole xml docuemnt
    - you can read and write
    - used by web browsers
    - js and jquery use DOM, in python there are 2 modules: xml.dom.minidom, xml.dom.pulldom

each node in dom has 3 parts: element, attribute, text 

elements have name, attributes have name and value, text have value (??)


## 1.3 reading xml in phyton 

parsers: 

xml.dom.minidom (built in)
xml.sax
untangle
beautifulSoup --> for web scraping 

DOM objects: node, document, nodeList, element 

it's also possible to use Js to parse xml: getElementById
Js can read from webpages and modify them. 
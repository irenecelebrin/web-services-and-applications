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
- SAX: simple API for XML 
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

Importing the data: 
1. from file --> 

filename = 'employees.xml"

doc = parses(filenam)

OR

with open (filename) as fp: 
    doc = parse(fp)


2. from url 

url = www.filename.xml
page = requests.get(url)

doc = parseString(page.content)

Then verify

print(doc.toprettyxml(), end = '')


**DOM PACKAGE** 

1) node: other objects inherit from this. It has type, name and value. 
Useful methods: 
- firstChild
- nodeValue
- others: parent

2) document: the root element. Methods
- getElementbyTagName(tagName)

3) NodeList: a List of Nodes, it is iterabe. Methods: 
- item(i)

Element: Normal element. Methods: 
- getElementsbyTagName(tagName)

FULL LIST --> see documentation https://docs.python.org/3/library/xml.dom.html 

Navigating down the tree

start from rootnode, navigate to the node, get the items and specif items using the index. If you want the text, get nodeValue.strip()
Text is another element of the tag, not another node. 

see wsaa2.3-xmlfromfile.py

GETTING XML with JAVASCRIPT
it's also possible to use Js to parse xml: getElementById
Js can read from webpages and modify them. 

## 1.4 JSON

Json: js object notation
hamn readable 
open standard
data is nested 
standard format to exchange data on the we 

similar to pyton dict, but quotes are always double. --> silly.json

Very flexible:

you can have objects inside json (in js)

**Json pckage in python**
in python there is a json package: 
- dump: dump dict jbj into file as json
- dumps: dump dict into file as string 
- load: load json into python dict
- loads: take json string and give back json object 

**read json from file**
with open('filename', 'r) as fp:
    jsonobect = json.load(fp)

From the cloud use requests

**read json from url**
url = ..
response = requests.get(url).text
data = json.loads(response)

or
url == ""
response = requests.get(url).json()


ALT SHIFT S to pretty json format in the code editor 

see list of APIs in the references 

# 2 Data transfer 

## 2.1 HTTPS and URL / 2.2 HTTP METHODS 

Used to get data from informaiton on the cloud 

You use the requests module to get urls 

response = requets.get(url)

**what is HTTP**
way of transferring data among computers 
1.0, 1.1, 2.0
usually http works on port 80 

from your brwoser you make a request to a server. The server will send back a http rfesponse with a status line 
100-199 --> informational 
200 ok, 200-299 --> succesfull
300-399 --> redirection
404 not found, 400-499 client error
500-599 --> server error

200 ok
201 created 
204 no content 
400 bad syntex
401 unauthorized
403 forbidden
404 not found 
500 internal server error


html will be used to display the response 

https is a secures http 
request uses **GET** 
other info: version, type of browser, language, other encodings
you also need to specify if you want json putput 

**RESPONSE** inlcudes
response
date
sever
length
content type 
content

https methods: 
- get --> read --> params are visible to the user. Never use get when sending sensitive data like passswords 
- post --> create --> put data in the header of the request, parmas are not save in the history, cannot bookmark. 
- put --> update 
- patch 
- delete --> delete 
- options 
- head 

apart from this thing (params are saved / not saved), get and post can be used intercheangably. 

when you create an API, you want to have these methds 

URL: universal resource locator. Can be any type of object (image, music, text...)

Parts of url: 
- protocol : http, https, ssh (http/https used in restful APIs)
- host: atu.ie (name or IP address of the machine )
- resource: between host and params, ends with ? 
- paramteres. After the question mark, name-value pairs separated by = 

**Encoding** 
special characters (for example spaces) need to be replace (encoded)

space = %20
" = %22 

some functions encode characters automatically 

**how to generate a http request?** 

Browser
curl
postman
python (request object)
js (ajax)
other languages 

**See source code**
Use "developer tools" to view the source code (html + js)

you can see the response and html code
+ a lot of other links --> images and css, which contribute to the design of the website 

before it was only 1 resposne, now js is used to pull from multiple https websites, for the same web page 

You can access and change everything that is displayed (clearly once you refresh the page, your chnages will be lost). 

**CURL**
comes with most OSs.

type in command 
curl -i atu.ie  --> shows response

curl https://https.atu.ie --> shows all the content 

**POSTMAN** download on your machine 
You can see the same content as in the developers tool 

**REQUESTS**
in python, to get the content of a web page 

## 2.3 Restful APIs

How to use HTTPS to make an API 

API applicatp programming interface. way to trasnfer data. 

Restful APIs: program passing info to prohram using the cloud 

**Soap** ==> trasnferring data through xml. Very rarely used now. 
Developed by microsfoft

**Restful** representation State Transfer

- mostl https apis are not restful 
- restful apis used multiple methods, not just get and post 
- restful apis have contraints: cacheable, stateless 
- idempotency --> requests cannot be made twice, each request comes with a key

REST example: 
GET --> get everything
POST --> create an email 
GET --> get based on criteria (this can be a FIND by XX function)
PUT --> modify something 
DELETE --? delete something

** remember to escape out inverted commas on windows machines 

goal of the module --> create and API 

**stateless** 
**chacheable** (transparent)

Sites that use apis: facebook, google, stripe, cso 

see response indformation in developer tool / network

open anderewbeatty link
open page with books
you can use postman to update and add a new book 
you can click on POST and send the change 

## 2.4 CURL 

- Client side URL
- used to call a URL and retrieve the response. It was used for webscraping before python 
- built in windows 10 and mac

Options: 
curl -i to see repsonse header
curl -x <method> to set the method. for example curl -X delete 
curl -d <data> set the data to be uploaded 
curl -H <header> to set the header 

on Windows you need to escale double quotes 

see slides for actions to create the API with curl 

curl is more basic than postman to use 

try: curl andrewbeatty1.pythonanywhere.com/books 

curl andrewbeatty1.pythonanywhere.com/books/574
if the book id does not exist, you either get a message or internal error

curl -H "Content-Type:application/json" -X POST -d "{\"titke\":\"by curl\",\"author\":\""\,\"price\":\"xx\"} andrewbeatty1.pythonanywhere.com/books

if you make a misrakte doing it, you get a 500 error

all this stuff you can do with postman, too. 


# 3. Reading APIs in the wild 

Some in the code in courseware is titled 'topic 4' because this was topic 4 last year 

## 1. write a code to interact with an API + LAB 3

Interacting with externatl APIs using python and requests 

see github.com/psf/requests 

vert powerful: sessions, cookies, keep alive, auteentications

parameters: 

- headers
- data types
- json

response attributes and methods: 
- status_code
- text
- json()
- content
- header()

URL ENCODING

python module: urllib.parse

quote() function to turn any string into a url encodeed string 

You can encode an url but also parameters

EXERCISE: get data from an API 
Best practice: create the code in functions, so that a function gets the data and a function analyses the data.

See documentation for 

requests.get(url) 
requests.post(url, params) --> https://www.w3schools.com/python/ref_requests_post.asp 
requests.put(url, params) --> to update https://www.geeksforgeeks.org/python/put-method-python-requests/ 
requests.delete(url, params)

Also in the slides 

## 2. Reading data from data.gov.ie

Real APis --> there is no one system, you need to find the way based on the data, reading documentation, authorizations, limits... 

Consider: 
- rate limits
- authentication: API keys, Oauth
- format of responses: mostly json, somethimes xml, sometimes some data is invalid/missing
- validity of data 
- sometimes urls change and your code won't work until you fix that 

sources:
data.gov.ie/dataset
cso.ie (in video 3)

on DATA.GOV.IE
see national planning applications
you can preview the data before downloading it (sometimes). 

see 4.2-planning.py

## 3. Reading data from CSO.ie 

CSo provides data in a json format called pxtat, which is used for multidimentional data. 
Decent module to use pxtat??
we are looking at restAPI not Json rpc

go to cso.ie/databases
PxStat: Horrid format, a json format which allows for multidimensional data 
documentation on cso website
documentation: github.com/CSOIreland/PxStat/wiki/API-Cube-RESTful 

Requests.get gives a huge jason with: 
- values as an array
- ods as array of each dimension
- sizes (as array) of each dimension
- dimensions (object) stores information about each dimention
- other information and notes 

ID: ids of the dimenions
size: size if the dimentions
value: all the data 
labels: provide info on the number of data points for each dimension 

sometimes data for each dimension is not in the same order, not everything correspondds: for example, you can have x data points for each dimension. You can remap considering all these things and embedding in a new structure 

Watch video to parse pxstat in normal json!!









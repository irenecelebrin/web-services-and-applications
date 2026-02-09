## lab 2
## Author: irene celebrin
## Date: 2026-02-02

# prints the data for all trains in Ireland to the console.

import requests
import csv
from xml.dom.minidom import parseString

url = "https://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)

# parse xml with minidom. https://docs.python.org/3/library/xml.dom.minidom.html
doc = parseString(page.content)

# print data in the console
# print(doc.toprettyxml())

# save the data to xml file
#with open('trains.xml', 'w') as fp:
   #doc.writexml(fp)


# select and print all train codes. dom documentation: https://docs.python.org/3/library/xml.dom.html  
train_position_nodes = doc.getElementsByTagName('objTrainPositions')

for train_position_node in train_position_nodes:
    train_code_node = train_position_node.getElementsByTagName('TrainCode').item(0)
    train_code = train_code_node.firstChild.nodeValue
    # print(train_code)



# print out train latitutdes (alternative method)

for train_position_node in train_position_nodes:
    train_latitude_node = train_position_node.getElementsByTagName('TrainLatitude').item(0)
    train_latitude = train_latitude_node.firstChild.nodeValue
    # print(train_latitude)



# write all data to a csv 
with open('lab1_trains.csv', 'w', newline='') as train_file:
    train_writer = csv.writer(train_file)

    retrieval_tags = ['TrainStatus', 'TrainLatitude', 'TrainLongitude', 'TrainCode', 'TrainDate', 'PublicMessage','Direction']

    
    train_data = []
    for train_position_node in train_position_nodes:
        for retrieval_tag in retrieval_tags:
            data_node = train_position_node.getElementsByTagName(retrieval_tag).item(0)
            train_data.append(data_node.firstChild.nodeValue.strip())
        train_writer.writerow(train_data)
        train_data = []
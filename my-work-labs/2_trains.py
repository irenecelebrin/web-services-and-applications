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

train_codes = doc.getElementsByTagName("TrainCode")
train_latitudes = doc.getElementsByTagName("TrainLatitude")

print(train_codes[0].firstChild.nodeValue)


with open("trains.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["TrainCode"])
    for code in train_codes:
        writer.writerow(code.firstChild.nodeValue)


'''
with open("trains.xml", "w") as xmlfp:
    doc.writexml(xmlfp)
'''



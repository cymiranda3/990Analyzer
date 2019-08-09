import xml.etree.ElementTree as ET
import requests
import os

os.system("irsx --format=csv --file='puget.csv' 201331309349302878")

# def loadRSS():
#     # url of rss feed
#     url = 'https://s3.amazonaws.com/irs-form-990/201741319349303099_public.xml'
#
#     # creating HTTP response object from given url
#     resp = requests.get(url)
#
#     # saving the xml file
#     with open('990.xml', 'wb') as f:
#         f.write(resp.content)
#
# def parseXML(xmlfile):
#     tree = ET.parse(xmlfile).getroot()
#
#     test = [elem.tag for elem in tree.iter()]
#     print(test.find("ScheduleD"))
#
# parseXML('990.xml')

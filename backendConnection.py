import xml.etree.ElementTree as ET
from Message import *
import time
from time import mktime
from datetime import datetime
import urllib3
import certifi
from base64 import b64encode
import json

class CTDRequest:
    #URLS
    urlCTD = 'https://slel00543677f.sle.sap.corp/sap/opu/odata/sap/zegodata_srv/'
    theurlCust = 'https://slel00543677f.sle.sap.corp/sap/opu/odata/sap/ztrmtodata_srv_01/TasksSet/?$format=json'  # Raspberry Vhs

                     
    userPass = b'I848072:*V8t8rctd*'

   
    
    def __init__(self):
        #Add Certificates
         self.http = urllib3.PoolManager(
            cert_reqs='CERT_NONE'
            #cert_reqs='CERT_REQUIRED', # Force certificate check.
            #ca_certs=certifi.where()  # Path to the Certifi bundle.
            )
         print certifi.where()

    def authenticateUser(self, rfid, device):
	args = "NamesSet(rfid='" + rfid + "',device='" + device + "')/?$format=json"
	url = CTDRequest.urlCTD + args
	print url
        return self.__callURL(url)

    def __callURL(self, url):
        #Basic authentication user and password
        userAndPass = b64encode(self.userPass).decode("ascii")

        print "user pass" + self.userPass
        
	headers = { 'Authorization' : 'Basic %s' %  userAndPass }
	print headers


        print 'Request 1'

        r = self.http.request('GET', url, headers=headers)
                              
        #pagestring = ""
        pagestring = json.loads(r.data)
        #print (pagestring)
	print json.dumps(pagestring, indent=4, sort_keys=True)
        
        

	print 'Request 2'

        #Change XML encoding
        #pagestring = pagestring.replace(b'encoding="utf-16"',b'encoding="utf-8"')
        #Get Components result
        #print (pagestring)

	#print 'Request 2.1'

        #root = ET.fromstring(pagestring).iter('RESULTNODE1')

	#print 'Request 3'

        #msgList = []

        #Retrieve Data
        #for result in root:
            
        #    for msg in result.findall('_-SID_-CN_IF_DEVDB_INC_OUT_S'):
        #        msgList.append(Message(
        #            msg.find('OBJECT_ID').text,
        #            msg.find('MESSAGE_NO').text,
        #            msg.find('DESCRIPTION').text,
        #            msg.find('STATUS_KEY').text,
        #            msg.find('PRIORITY_KEY').text,
        #            self.convertXmlDate(msg.find('CREATE_DATE').text),
        #            self.convertXmlDate(msg.find('CHANGE_DATE').text),
        #            self.convertXmlDate(msg.find('IRT_EXPIRY').text),
        #            self.convertXmlDate(msg.find('MPT_EXPIRY').text),
        #            msg.find('PROCESSOR_ID').text,
        #            msg.find('PROCESSOR_NAME').text,
        #            msg.find('URL_MESSAGE').text,
        #            msg.find('CATEGORY').text))

        #return msgList

    def convertXmlDate (self, dateTime):
        if dateTime != '0':
            return datetime.fromtimestamp(mktime(time.strptime(dateTime,'%Y%m%d%H%M%S')))
        else:
            return dateTime
        

#req = BCPRequest()
#msgList = req.getCustomerMessages()

#for msg in msgList:
#    print (msg.messageNo)



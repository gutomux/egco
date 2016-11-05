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

                     
    userPass = b'ASA1_EGCO_GA:Palinka1'

   
    
    def __init__(self):
        #Add Certificates
         self.http = urllib3.PoolManager(
            cert_reqs='CERT_REQUIRED',
            #cert_reqs='CERT_REQUIRED', # Force certificate check.
            ca_certs="./certificate.cer"  # Path to the Certifi bundle.
            )
         #print certifi.where()

    def authenticateUser(self, rfid, device):
	args = "NamesSet(rfid='" + rfid + "',device='" + device + "',idemployee=''')/?$format=json"
	url = CTDRequest.urlCTD + args
	#print url
        return self.__getURL(url)


    def __getURL(self, url):
        #Basic authentication user and password
        userAndPass = b64encode(self.userPass).decode("ascii")
        
	headers = { 'Authorization' : 'Basic %s' %  userAndPass }

	print "Calling backend..."

        r = self.http.request('GET', url, headers=headers)
        
        #pagestring = json.loads(r.data)
        
	return r.data	

	#return (pagestring["d"]["name"])

    def createUser(self, rfID, deviceID, iNumber):
	print "Calling backend..."
	userAndPass = b64encode(self.userPass).decode("ascii")
	
	headers = { 'Authorization' : 'Basic %s' %  userAndPass }

	args = "UserCreate(rfid='" + rfID + "',device='" + deviceID + "',idemployee='" + iNumber + "')/?$format=json"
	#encoded_args = urlencode({'rfid': rfID, 'device': deviceID, 'idemployee': iNumber})
	url = CTDRequest.urlCTD + args
	print "url: " + url
	r = self.http.request('GET', url, headers=headers)
   	return r.data

    def makeContribution(self, weight, contributionTypeID, iNumber):
	userAndPass = b64encode(self.userPass).decode("ascii")
	headers = { 'Authorization' : 'Basic %s' %  userAndPass }
	args = "ContributionCreate(weight=" + weight + ",ctype='" + contributionTypeID + "',idemployee='" + iNumber + "')/?$format=json"
	url = CTDRequest.urlCTD + args
	print url
	r = self.http.request('GET', url, headers=headers)
   	return r.data

    def convertXmlDate (self, dateTime):
        if dateTime != '0':
            return datetime.fromtimestamp(mktime(time.strptime(dateTime,'%Y%m%d%H%M%S')))
        else:
            return dateTime
        

#req = BCPRequest()
#msgList = req.getCustomerMessages()

#for msg in msgList:
#    print (msg.messageNo)



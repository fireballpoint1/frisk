import requests

class VtAPI():
    def __init__(self, key):
        self.key = key

    def uploadScan(self, file_name, file_address):
        url = 'https://www.virustotal.com/vtapi/v2/file/scan'
        params = {'apikey': self.key}
        files = {'file': (file_name, open(file_address, 'rb'))}

        response = requests.post(url, files=files, params=params)

        return(response.json())

    def getScanReport(self, resource):
        url = 'https://www.virustotal.com/vtapi/v2/file/report'
        params = {'apikey': self.key, 'resource': resource}
        response = requests.get(url, params=params)
        return(response.json())

    def getBehaviourReport(self, hash): # needs a private key to be bought
        url = 'https://www.virustotal.com/vtapi/v2/file/behaviour'
        params = {'apikey':self.key,'hash':hash}
        response = requests.get(url, params=params)
        return(response.json())
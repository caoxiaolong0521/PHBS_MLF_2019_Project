# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:49:20 2020

@author: caoxiaolong
"""

import requests
import json

class SafeBrowse():
    def __init__(self, apikey):
        self.safe_base = 'https://safebrowsing.googleapis.com/v4/threatMatches:find?key=%s' % (apikey)
        self.platform_types = ['ANY_PLATFORM']
        self.threat_types = ['THREAT_TYPE_UNSPECIFIED',
                             'MALWARE', 
                             'SOCIAL_ENGINEERING', 
                             'UNWANTED_SOFTWARE', 
                             'POTENTIALLY_HARMFUL_APPLICATION']
        self.threat_entry_types = ['URL']

    def set_threat_types(self, threats):
        self.threat_types = threats

    def set_platform_types(self, platforms): 
        self.platform_types = platforms

    def threat_matches_find(self, *urls):   #urls is a tuple
        try:
            threat_entries = []  #list of dicts, which have a member, named URL, loading a str of url
            
            for url_ in urls: 
                url = {'url': url_} 
                threat_entries.append(url)

            request_body = {
                'client': {
                    'clientId': 'MLF-2019',
                    'clientVersion': '1.5.2'
                    },
                'threatInfo': {
                    'threatTypes': self.threat_types,
                    'platformTypes': self.platform_types,
                    'threatEntryTypes': self.threat_entry_types,
                    'threatEntries': threat_entries
                    }
                }
            
            headers = {'Content-Type': 'application/json'}
            r = requests.post(self.safe_base,
                              data=json.dumps(request_body),
                              headers=headers, timeout=2)

            jdata = r.json()
            #print(jdata['matches'][0]['threatEntryType'])
            
            # If the threatEntryType matches the string URL, the parsed URL
            # has been classified as not safe by Google. In this case a 1
            # is returned and otherwise a 0 is returned.
            if jdata['matches'][0]['threatEntryType'] == 'URL':
                return 1 # Malicious
            else:
                return 0
        except:
            return 0
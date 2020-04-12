# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 10:35:20 2020

@author: He Jinze
"""
import math
from sklearn.feature_extraction.text import CountVectorizer
import re
import pandas as pd
from SafeBrowse import SafeBrowse
#%% parse_url
def parse_url(url):
    if 'http://' in url:
        return url.split('http://', 1)[-1]
    elif 'https://' in url:
        return url.split('https://', 1)[-1]
    else:
        return url
#%% URLFeature
class URLFeatures():
    def __init__(self, url):
        self.url = url
    
    def Entropy(self):
        if not self.url:
            return 0
        entropy = 0
        chars = set(list(self.url))
        length = len(self.url)
        for i in chars:
            p_x = self.url.count(i)/length
            entropy += - p_x*math.log(p_x, 2)
        return entropy
    # Bag Of Words method is used for text analysis.
    # Here URLs are described by word occurrences while completely 
    # ignoring the relative position information of the words in  the document.
    def bag_of_words(self):
        vectorizer = CountVectorizer()
        content = re.split('\W+', self.url)
        X = vectorizer.fit_transform(content)
        return X.shape[1]
    
    # Contains IP method to check the occurence of an IP address within a URL.
    def contains_IP(self):
        check = self.url.split('/')
        reg = re.compile("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")
        for item in check:
            if re.search(reg, item):
                return 1
        return 0
    
    # URL Length method to calculate the URL length.
    # Malicious URLs can often be very long in comparrison to benign URLs.
    def url_length(self): return len(self.url)
    
    # Special Characters method to check for specific special chars.
    # Sometimes Malicious URLs contain a higher number of special characters.
    # In this method, a counter is used to count the number of special characters 
    # that are found within a URL.
    def special_chars(self):
        counter = 0
        str_list=['*',';','%','!','&',':']
        for i in str_list:
            counter += self.url.count(i)
        return counter

    # Suspicious Strings method to check for suspicious strings within the URLs.
    # A higher number of suspicious strings would indicate a possibly malicious URL. 
    def suspicious_strings(self):
        '''
        '.exe': Malicious URLs may contain the string '.exe' in reference to downloading a possibly malicious executable.
        'base64': Malicious URLs may use base64 encoding to encode and possibly obfuscate information.
        '/../' & '.pdf': The occurence of '/../' may possibly indicate file inclusion.
        'free' & 'Free' & 'FREE': Fishing can use social engineering to lure victims to click on malicious links. The use of the word free may be included within URLs to trick users in visiting malicious websites.
        '.onion' & '.tor': references the use of tor.
        '.top' & '.bid' & '.ml': Such domains are suspicious and according to RFC 7686 should be kept off public internet.
        'bitcoin' & '.bit' & '.php?email=': Bitcoin references.
        'cmd=': Possible command execution.
        Parameters
        ----------
        url : str
            URL string

        Returns
        -------
        counter : int
            Total number of suspicious_strings.
        '''
        counter = 0
        str_list=['.exe', 'base64', '/../', '.pdf', 'free', 'Free',
                  'FREE', '.onion', '.tor', '.top', '.bid', '.ml',
                  'bitcoin', '.bit', '.php?email=', 'cmd=']
        for i in str_list:
            if i in self.url: counter +=1
        return counter

    # Number Of Digits method returns the number of digits contained within a URL.
    # Malicious URLs often have a higher entropy and can contain lots of numbers.
    def num_digits(self):
        return sum([i.isdigit() for i in self.url])

    # Popularity method checks the url popularity against the top 1 million urls 
    # contained within the umbrella dataset.
    # Sites contained within this dataset are not malicious.
    def popularity(self):
        domain = self.url.split('/', 1)[0]
        if domain in top_website.values:
            return 1
        else:
            return 0
    def features(self):
        feature_list = [self.url, self.Entropy(), self.bag_of_words(),
                        self.contains_IP(), self.url_length(),
                        self.special_chars(), self.suspicious_strings(),
                        self.num_digits(), self.popularity()]
        return feature_list
#%% Extract Features
def extract_features(url):
    # Parses input URL to remove http:// or https://.
    # The umbrella dataset does not contain this and thus, is not required for certain feature extractions.
    parsed_url = parse_url(url)
    # Initiate a calculator to get features from class URLFeatures
    calculator = URLFeatures(parsed_url)
    # Appends URL to features list.
    features=calculator.features()
    apikey = 'AIzaSyBcXN17mB-qK1ccgqM4jy0LTjuSXKXN1Tc'
    safe = SafeBrowse(apikey)
    response = safe.threat_matches_find(url)
    features.append(response)
    # Returns extracted features from features list.
    return features
#%% Create_dataset
def create_dataset():
    output_file = "data_urls.csv"
    csv_delimeter = '|'
    csv_columns = ["URL","Entropy","BagOfWords","ContainsIP","LengthURL",
                   "SpecialChars","SuspiciousStrings","NumberOfDigits",
                   "Popularity","Safebrowsing","Malicious"]
    # Opens file that features will be written to for reading.
    feature_file = open(output_file, 'a')
    # Writes the feature column names to csv file. 
    feature_file.write(csv_delimeter.join(csv_columns) + "\n")
    # Opens the malicious URLs file for reading and creates a list
    # that contains all the rows (URLs) from the file.
    malicious_urls = pd.read_csv('malicious_urls.csv', squeeze = True,
                                  usecols = ['URL'])
    benign_urls = pd.read_csv('benign_urls.csv', squeeze = True, usecols = ['URL'])
    for i, url in enumerate(malicious_urls):
        try:
            features = extract_features(url)
        except:
            print("Error: extract features index: {0:d}, m_url: {1:s}.\n".format(i, url))
        features.append(1)
        feature_file.write(csv_delimeter.join(map(lambda x: str(x), features)) + '\n')
        if (i+1)%10==0:
            print('malicious: {0:d}/5000'.format(i+1))
    
    for i, url in enumerate(benign_urls):
        try:
            features = extract_features(url)
        except:
            print("Error: extract features index: {0:d}, b_url: {1:s}.\n".format(i, url))
        features.append(0)
        feature_file.write(csv_delimeter.join(map(lambda x: str(x), features)) + '\n')
        if (i+1)%10==0:
            print('benign: {0:d}/5000'.format(i+1))
    feature_file.close()
#%% Main
top_website = pd.read_csv('top1m_rank.csv', delimiter='|', usecols = ['URL'], squeeze = True)
create_dataset()
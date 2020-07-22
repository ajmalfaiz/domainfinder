import requests
import random
import string
import urllib3
import sys
import json


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
domains_available = [];
letterwords=[];
with open("words_alpha.txt") as word_file:
    valid = set(word_file.read().split())
for valid_words in valid:
    if len(valid_words)==6:
        letterwords.append(valid_words)
for word in letterwords:
    letters = string.ascii_lowercase
    domain = word
    URL = "https://www.domainnamesoup.com/cell3.php?pt=85"
    PARAMS = {'domain': domain+'.com'} 
    r = requests.get(url = URL, params= PARAMS, verify=False)
    if r != '':
        data = int(r.text)
    else: 
        data = 52
    if data == -1:
        availability = 'Wow, that is an Available domain'
        domains_available.append(domain)
        todisplay = domain + '\n'
        open(f"dictionary_search_6.txt", 'a').write(todisplay)
    else: 
        availability = 'Not available'
    print(f" {domain} :  {availability}")
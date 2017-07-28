#!/usr/local/bin/python2.7

import requests
from bs4 import BeautifulSoup

r = requests.get('http://feriados.cl/')
if(r.status_code != 200):
    print("Error getting the data")
    exit()
s = BeautifulSoup(r.text, 'html5lib')

s.select('table')[4].select('tr')[4]

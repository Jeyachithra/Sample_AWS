# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 20:25:17 2020

@author: Chitra
"""


import requests 
from bs4 import BeautifulSoup 
  
URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL) 
#print(r.content)
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib 
print(soup.prettify()) 
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 15:48:02 2020

@author: Chitra
"""

"""
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReg

my_url = "https://www.flipkart.com/search?q=iphone&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_5_6_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_5_6_na_na_na&as-pos=5&as-type=RECENT&suggestionId=iphone&requestId=6b65e353-1235-49a4-a2a5-30463900a995&as-searchtext=iphone"

uClient = uReg(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html,"html.parser")

containers = page_soup.findAll("div",{"class":"_4rR01T"})
for i in containers:
    print(i.string)
"""


from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReg
import requests

query=input("query>>")
query=query.strip().split()
query="+".join(query)

my_url = "https://www.google.co.in/search?site=&source=hp&q="+query+"&gws_rd=ssl"
#my_url = "https://www.flipkart.com/search?q=iphone&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_5_6_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_5_6_na_na_na&as-pos=5&as-type=RECENT&suggestionId=iphone&requestId=6b65e353-1235-49a4-a2a5-30463900a995&as-searchtext=iphone"
"""
uClient = uReg(my_url)
page_html = uClient.read()
uClient.close()"""
res = requests.get(my_url)
if res.status_code == 200:
    print("Successfull downloading html")
    page_soup = soup(res.content,"html.parser")
    containers = page_soup.findAll("h2")
    #containers = page_soup.findAll("div",{"class":"kp-wholepage kp-wholepage-osrp HSryR EyBRub"})#"Kot7x"
    print(containers)
    #for i in containers:
    #    print(i.string)
    
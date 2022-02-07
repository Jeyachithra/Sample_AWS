# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 14:20:28 2020

@author: Chitra
"""
import requests,sys,webbrowser,bs4


html = "https://en.tutiempo.net/india.html"
res = requests.get(html)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.content, "lxml")#'html5lib'
titles = soup.find_all("div",attrs={"class":"TopLocPie"})
print(titles)
print("Hello this is second one")
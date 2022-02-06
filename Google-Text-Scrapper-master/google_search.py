# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 19:18:21 2020

@author: Chitra
"""
import requests,sys,webbrowser,bs4

#Forming query
query=input("query>>")
query=query.strip().split()
query="+".join(query)

html = "https://www.google.co.in/search?site=&source=hp&q="+query+"&gws_rd=ssl"
res = requests.get(html)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.content, "lxml")#'html5lib'
#print(soup.prettify()) 




# name the output file to write to local disk
out_filename = "D://Halethee//web scraping//python-google-scraping-master//raw_ingre.csv"
# header of csv file to be written
headers = "title,measurements,info \n"
#Result is Displayed

# opens file, and writes headers
f = open(out_filename, "w")
f.write(headers)
#f.write(str(x) + title.get_text()+"\n" )
f.close()
#title_elem = soup.find('span', class_='title')
#print(title)
job_elems = soup.find_all('div', class_='Kot7x')#
print(job_elems)
for elem in job_elems:
   
    company_elem = elem.find('table', class_='AYBNrd')
    location_elem = elem.find('div', id='kno-nf-nc')
    print("Jaya Info\n\n\n")  # print(title_elem)
    print(company_elem)
   # print(location_elem)

"""
soup = bs4.BeautifulSoup(res.text,"html.parser")
linkElements = soup.select('.r a')
linkToOpen = min(5,len(linkElements))
for i in range(linkToOpen):
    webbrowser.open('https://google.com'+linkElements[i].get('href'))
    
"""
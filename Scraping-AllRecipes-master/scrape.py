# -*- coding: utf-8 -*-
"""
Takes a list of URLs from allrecipes.com

@author: Derek
"""

from urllib.request import urlopen
#import pandas as pd
from bs4 import BeautifulSoup
import re
import pickle
# from sys import setrecursionlimit
import json
import gc

# use pickle to import the scraped URLs from scrapeURLs.py
urlList = pickle.load(open("urlList.p", "rb"))
#urlList = [line.strip() for line in open('urlList.txt')]


# delete repeats
urlList = list(set(urlList))
#urlList2 = urlList[0:1000]
urlList2 = urlList[0:99]
print(urlList)

i = 0
dictionaryList = []

for url in urlList2:
    i += 1
    print(i)
    print(url)
    # clear dictionaryTemp
    dictionaryTemp = {}
    
    #Query the website and return the html to the variable 'page'
    page = urlopen(url)
    #Parse the html in the 'page' variable, and store it in Beautiful Soup format
    soup = BeautifulSoup(page, "lxml")
    
    # print(soup.prettify())
    
    # return content between openeing an closing tag, including tag
    # soup.span.recipe-ingred_txt.added
    htmlIngredients = soup.find_all('span', {'class': "recipe-ingred_txt added"})
    htmlIngredients
    
    # grab directions using the same method 
    htmlDirections = soup.find_all('span', {'class': "recipe-directions__list--item"})
    htmlDirections[0].text
    
    # make empty list for ingredient list
    ingredientList = []
    ingredientIdList = []
    # iterate throught the list of tags to extract the ingredients
    for ingredient in htmlIngredients:
        ingredientList.append(ingredient.string)
        
        temp = re.search('(?<=data-nameid=")(\d*)(?=")', str(ingredient)).group(1)
        ingredientIdList.append(temp)
        
    # htmlRating = soup.find_all('div', {'class': 'recipe-summary__stars'})
    htmlRating = soup.find_all('span', {'itemprop': 'aggregateRating'})
    strRating = re.search('(?<=content=")(.*)(?=" itemprop="ratingValue")',
                          str(htmlRating)).group(1)
    strReviews = re.search('(?<=content=")(.*)(?=" itemprop="reviewCount")',
                          str(htmlRating)).group(1)
    
    
    # get the title
    title = soup.find_all("h1", {'class': "recipe-summary__h1"})[0].text
            
    dictionaryTemp = {"Food": title,
                      "Rating": strRating,
                      "Reviews": strReviews,
                      "Ingredient List": ingredientList,
                      "Ingredient IDs": ingredientIdList,
                      "URL": url}
            
    dictionaryList.append(dictionaryTemp)


#del temp, dictionaryTemp, ingredientIdList, ingredientList, strRating,strReviews,title, url
    
del urlList, urlList2, i
 

# this makes a ~600 mb file for just 1000 recipes. Use JSON instead.
#setrecursionlimit(10000)
#pickle.dump(dictionaryList, open( "dictionary.p","wb" ))
#setrecursionlimit(1000)
   
with open("dictionary0-1000.json","w") as f:
    json.dump(dictionaryList,f)
    
del dictionaryList
gc.collect()

# test to see if it loads properly    
#text = open("dictionary0001-1000.json", "r").read()
#dictionaryListLoad = json.loads(text)
#text = open("dictionary1001-4000.json", "r").read()
#dictionaryListLoad1 = json.loads(text)

#df = pd.DataFrame.from_dict(dictionaryList)  
    
# use pandas to convert list to data frame
#df = pd.DataFrame(title,columns=['Title'])
#df['Rating']=strRating
#df['# of Reviews']=strReviews
#df['URL']=url
#df['Ingredients']=ingredientList
#df['Ingredient ID List']=ingredientIdList
#
#df


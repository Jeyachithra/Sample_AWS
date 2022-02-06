from imp import IMP_HOOK
import requests		# Requests required to obtain webpage
import bs4		# BS4 required to parse webpage
import json
IMP_
#Title Text Block
print("GOOGLE SCRAPING USING PY3 AND BS4 \n")

#Accepts Search Keywords from the User
query = input("ENTER SEARCH KEYWORDS: ")

query=query.strip().split()
query="+".join(query)

html = "https://www.google.co.in/search?site=&source=hp&q="+query+"&gws_rd=ssl"


#Setting Query Parameters for Search 
#params = [('q',keyword)]
try:
    #Google Search URL
    #url = "https://google.co.in/search"
    #url = "https://www.google.co.in/search?site=&source=hp&q="
    
    # Gets response from the server for the search query
   # response = requests.get(url=url, params=params)
    print(html)
    response = requests.get(html)
   # Now we need to check if the request was successfully.  If it returns a 200 , then it was successfully
    if response.status_code == 200:
        # Response text from server is parsed using bs4
     
        soup = bs4.BeautifulSoup(response.text,'lxml')
        
        titles = soup.find_all("div",attrs={"class":"liYKde g VjDLd"})
        print(titles)
        # print(containers.text)
          
        
     #   print(soup)
        for s in soup.find_all("div",attrs={"class":"liYKde g VjDLd"}):#"BNeawe vvjwJb AP7Wnd"
            print(s.text)
        
        
        all1=[]
        
        # Titles of results are found (Assumed that Google put h3 only on result titles) "BiYF3"
        for d in soup.findall("div", attrs={"class":"liYKde g VjDLd"}):
            """            
            name = d.find('span', attrs={'class':'zg-text-center-align'})
            n = name.find_all('img', alt=True)
            #print(n[0]['alt'])
            author = d.find('a', attrs={'class':'a-size-small a-link-child'})
            rating = d.find('span', attrs={'class':'a-icon-alt'})
            users_rated = d.find('a', attrs={'class':'a-size-small a-link-normal'})
            """
            print("\n\n\n Enter here")
            name = d.find('span', attrs={'class':'kno-nf-sbl'})
            n = name.find_all('tittle', alt=True)
            print("Name of the food",n)
            rating = d.find('span', attrs={'class':'kno-nf-sbl'})
            price = d.find('span', attrs={'class':'kno-nf-sbl'})
    
           
            
            if name is not None:
                #print(n[0]['alt'])
                all1.append(n[0]['alt'])
            else:
                all1.append("unknown-product")
                
            
            
            if price is not None:
                #print(price.text)
                all1.append(price.text)
            else:
                all1.append('0')
            
            alls.append(all1)
    
            if name is not None:
                #print(n[0]['alt'])
                all1.append(n[0]['alt'])
            
            
            
            
            
            titles = soup.find_all("h3")
            #print(attributes.text)
           # print(containers.text)
            
            dictionaryList = []
            
            result = []
            
            print("\nDISPLAYING FIRST PAGE RESULT TITLES FOR " + keyword + "\n")
            
            x = 0; # counter variable
            for title in titles: #loop to display titles
                x=x+1 # counter updated
                print( str(x) + ". " + title.get_text() ) 
                dictionaryTemp = {"Food": title.get_text() }
                dictionaryList.append(dictionaryTemp)
            
            for attribute in containers:
                 info = attribute.text.split(":",1)
                 result.append([search_key, info[0].lower().replace("–","-"), info[1].lower().replace("–","-")])
            
                
            print(result)    
            with open("D://Halethee//web scraping//python-google-scraping-master//raw_ingre.json","w") as f:
                json.dump(dictionaryList,f)
                
            del dictionaryList
            #gc.collect()
except Exception as ex:
    print("Error",str(ex))
finally:
    print("Scrapping Success")
    #return g_clean


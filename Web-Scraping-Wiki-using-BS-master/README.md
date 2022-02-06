# Web-Scraping-Wiki-using-BS
In this project, I've attempted to learn and implement the basics of web scraping using the Python library, Beautiful Soup to scrape content from a Wikipedia page containing the list of all aircraft accidents and incidents resulting in at least 50 fatalities.

**URL: https://en.wikipedia.org/wiki/List_of_aircraft_accidents_and_incidents_resulting_in_at_least_50_fatalities

The list of 549 records containing 13 variables (columns) are available in a table which I've scraped using the BeautifulSoup library in Python.

Inspecting the HTML of the Wikipedia page, it can be observed that the text in the first 5 columns, related to Deaths are available within the 'th' tags of the table, while the text in the rest of the columns is available within the 'td' tags.

The data from the first 5 columns with the 'th' tags has been extracted into one dataframe and the data from the rest of the columns with the 'td' tags into another dataframe. Both the dataframes have then been concatenated to form a single dataframe.

I've referred to several websites and blogs to understand the basics of web scraping and using the BeautifulSoup library along with the BS4 documentation.

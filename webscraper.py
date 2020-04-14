# WEB SCRAPER 101

import requests
import csv
import json


page_number = 0
quote_number = 0

json_content = True


with open('scrape.csv', 'w') as csvfile:
    columns = ['author', 'type', 'quote']
    writer = csv.DictWriter(csvfile, fieldnames = columns)

    writer.writeheader()
    while json_content == True:
        page_number += 1
        content = requests.get('http://quotes.toscrape.com/api/quotes?page={}'.format(page_number)).json()
        content = content["quotes"]
        print(content)
        json_content = False

                            

        #if content != []:
            #for quotes in content:
                #quote_number += 1
                #print(quote_number)
                #author = quotes["author"]["name"].encode("utf-8")
                #try:
                    #type = quotes["tags"][0].encode("utf-8")
                #except:
                    #type = "Unspecified"







                            
                    
                                    

                    








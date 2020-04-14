# WEB SCRAPER

import requests
import csv
import json


page_number = 0

json_content = True


with open("scrape.csv", "w", encoding="utf8") as csvfile:
    columns = ["author", "tag", "quote"]
    writer = csv.DictWriter(csvfile, fieldnames = columns)

    writer.writeheader()
    while json_content == True:
        page_number += 1
        content = requests.get('http://quotes.toscrape.com/api/quotes?page={}'.format(page_number)).json()
        content = content["quotes"]
        print(page_number)
        quote_number = 0

        if content != []:
            for quotes in content:
                quote_number += 1
                print(quote_number)
                author = quotes["author"]["name"]
                try:
                    tag = quotes["tags"][0]
                except:
                    tag = "Unspecified"
                quote = quotes["text"]
                di = {"author":author, "tag":tag, "quote":quote}
                writer.writerow(di)
        else:
            json_content = False
            print("Scrape complete!")

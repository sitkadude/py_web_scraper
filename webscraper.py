# WEB SCRAPER

import requests
import csv
import json


page_number = 0
quote_number = 0

json_content = True


with open("scrape.csv", "w") as csvfile:
    columns = ["author", "tag", "quote"]
    writer = csv.DictWriter(csvfile, fieldnames = columns)

    writer.writeheader()
    while json_content == True:
        page_number += 1
        content = requests.get('http://quotes.toscrape.com/api/quotes?page={}'.format(page_number)).json()
        content = content["quotes"]
        print(content)               

        if content != []:
            for quotes in content:
                quote_number += 1
                print(quote_number)
                author = quotes["author"]["name"].encode("utf-8")
                try:
                    tag = quotes["tags"][0].encode("utf-8")
                except:
                    tag = "Unspecified"
                quote = quotes["text"].encode("utf-8")
                di = {"author" : author, "tag" : tag, "quote" : quote}
                writer.writerow(di)
        else:
            json_content = False
            print("Scrape complete!")

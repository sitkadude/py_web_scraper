# WEB SCRAPER

# DEPENDENCIES
import requests
import csv
import json


page_number = 0
json_content = True

# CREATE FILE OBJECT
with open("scrape.csv", "w", encoding="utf8") as csvfile:
    # CREATE ARRAY TO ASSIGN TO fieldnames PARAMETER
    columns = ["author", "tag", "quote"]
    # CREATE OBJECT THAT MAPS DICTIONARIES ONTO OUTPUT ROWS
    writer = csv.DictWriter(csvfile, fieldnames = columns)

    # WRITE ROW WITH fieldnames VALUES
    writer.writeheader()
    # WHILE LOOP TO BEGIN CONDITIONAL
    while json_content == True:
        page_number += 1
        # CREATE RESPONSE OBJECT
        content = requests.get('http://quotes.toscrape.com/api/quotes?page={}'.format(page_number)).json() content = content["quotes"] print(page_number) quote_number = 0

        # IF content DOES NOT EQUAL AN EMPTY LIST
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

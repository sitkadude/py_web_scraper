# WEB SCRAPER

# Dependencies
import requests
import csv
import json

page_number = 0
json_data = True

# Create file object.
with open("scrape.csv", "w", encoding="utf8") as csvfile:
    # Create an array to assign values to <fieldnames> parameter.
    columns = ["author", "tag", "quote"]
    # Create object that maps dictionaries onto output rows.
    writer = csv.DictWriter(csvfile, fieldnames = columns)

    # Write row with the values assigned to <fieldnames>.
    writer.writeheader()
    # Create while loop to begin conditional statement.
    while json_data == True:
        page_number += 1
        # Create a response object. Inspect element on website to find URL (which in this case was a JSON api).
        content = requests.get('http://quotes.toscrape.com/api/quotes?page={}'.format(page_number)).json() 
        content = content["quotes"]
        # This print function is merely to help me make sure my script is working on every page.
        print(page_number) 
        quote_number = 0

        # If <content> DOES NOT EQUAL an empty list..
        if content != []:
            # Iterate <quotes> through <content>.
            for quotes in content:
                quote_number += 1
                print(quote_number)
                # Assign the values that are paired to the following JSON keys to these variables.
                author = quotes["author"]["name"]
                try:
                    tag = quotes["tags"][0]
                except:
                    tag = "Null"
                quote = quotes["text"]
                # Explicitly map these values to the following dictionary keys.
                di = {"author":author, "tag":tag, "quote":quote}
                # Write these dictionary entries to the output file.
                writer.writerow(di)
        # Break loop.
        else:
            json_data = False
            print("Scrape complete!")

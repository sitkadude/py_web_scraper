# WEB SCRAPER 101

import requests
import csv
import json

csv_columns = ["Author", "Quote Type", "Quote"]
page_number = 0

jsonContent == True

with open('scrape.csv', 'w') as outfile:
    writer = csv.DictWriter(outfile, fieldnames = csv_columns)
    writer.writeheader()
    while jsonContent == True:
        page_number += 1
        count




# WEB SCRAPER 101

import requests
import csv
import json


page_number = 0

json_content == True


with open('scrape.csv', 'w') as csvfile:
    columns = ['Author', 'Type', 'Quote']
    writer = csv.DictWriter(csvfile, fieldnames = columns)

    writer.writeheader()
    while json_content == True:
        page_number += 1
        content = requests.get('http://quotes




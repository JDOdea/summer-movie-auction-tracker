import requests
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import csv
import json

# URL of the Box Office Mojo page for the weekend of June 5-7, 2026
url = "https://www.boxofficemojo.com/weekend/2026W23/?ref_=bo_wey_table_6"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)

# parses all <table> tags into a list of DataFrames
tables = pd.read_html(response.content)
# print(tables)

# test for saving to csv file
with open('box_office_mojo.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Rank', 'Title', 'Weekend Gross', 'Gross to Date'])
    for table in tables:
        for index, row in table.iterrows():
            rank = row[0]
            title = row[2]
            weekend_gross = row[3]
            gross_to_date = row[8]
            writer.writerow([rank, title, weekend_gross, gross_to_date])

# test for saving to JSON file
data = []
with open('box_office_mojo.json', 'w', encoding='utf-8') as json_file:
    for table in tables:
        for index, row in table.iterrows():
            rank = row[0]
            title = row[2]
            weekend_gross = row[3]
            gross_to_date = row[8]
            data.append({
                'Rank': rank,
                'Title': title,
                'Weekend Gross': weekend_gross,
                'Gross to Date': gross_to_date,
            })
    json.dump(data, json_file, indent=4)
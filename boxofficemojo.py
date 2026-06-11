import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.boxofficemojo.com/weekend/2026W23/?ref_=bo_wey_table_6"
headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url, headers=headers)

# parses all <table> tags into a list of DataFrames
tables = pd.read_html(response.content)
print(tables)
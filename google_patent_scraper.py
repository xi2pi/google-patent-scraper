# -*- coding: utf-8 -*-
"""
@author: Christian Winkler

Google Patent Scraper
"""

import requests
from bs4 import BeautifulSoup


patent_number = "EP3263425B1"

url = 'https://patents.google.com/patent/' + patent_number + '/en'
soup = BeautifulSoup(requests.get(url).content, 'html.parser')

for code in soup.select('[itemprop="Code"]:has(~ meta[itemprop="Leaf"])'):
    print(code.text)
    
text_file = open(patent_number + ".txt", "w", encoding='utf-8')
text_file.write(soup.text)
text_file.close()
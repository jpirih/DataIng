# Skripta prebere vse citate  
# Citate bere stran po stran dokler ne pride do konca 
# vse citate  najprej zložim od vsakega citata tekst in avtorja  v all_quotes = []
# Na koncu zapišem v Excel datoteko  all_quotes.xlsx s pomočjo pandas kjjižnice

import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "https://quotes.toscrape.com"

all_quotes = []

url = "https://quotes.toscrape.com"
next_page = True
        
while next_page:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.select('.quote')
    
    for quote in quotes:
        quote_data = []
        text_element = quote.select_one(".text")
        author_element = quote.select_one(".author")
        quote_text = text_element.get_text(strip=True)
        author = author_element.get_text(strip=True)
        quote_data.append(quote_text)
        quote_data.append(author)
        all_quotes.append(quote_data)
        
        next_link = soup.select_one(".next")
    
    if next_link:
        next_page = True
        page_link = next_link.select_one("a[href]")
        page_uri = page_link["href"]
        url = base_url + page_uri
    else:
        next_page = False
        

    
data = pd.DataFrame(all_quotes, columns=['Quote', 'Author'])
data.to_excel('all_quotes.xlsx', index=False)
    
print("\n All quotes")
print(data)
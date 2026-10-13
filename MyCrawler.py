import time
import requests
import re
from bs4 import BeautifulSoup
import json

url = "https://quotes.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
 
text = soup.get_text(separator=" ").lower()
print('-------------------')
word = input( "Enter a word that you want to find the occurences: ").lower()
clean_text = re.sub(r"[^\w\s]", " ", text)
words = clean_text.split()
print('-------------------')
count = sum(1 for w in words if w == word)
print(f"Occurrences found: {count}")
print('-------------------')
time.sleep(2)
quotes = soup.find_all('span', class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')
print('-------------------')
for x in range(len(quotes)):
    print(f'{quotes[x].text} - {authors[x].text}')
    time.sleep(0.1)
    print(f'{tags[x].text}')
    time.sleep(0.1)
    print('-------------------')
time.sleep(2)
stored_data = []
x = []
for a in range(len(quotes)):
    quote = quotes[a].text
    x.append(quote)
stored_data.append(x)

x = []
for b in range(len(authors)):
    author = authors[b].text
    x.append(author)
stored_data.append(x)
n = int(input("Enter the number of the quote you want to view between 1-10: "))
print(f"Quote: {stored_data[0][n-1]} - {stored_data[1][n-1]}")

print('-------------------')    
time.sleep(2)
for _ in range(len(quotes)):
    info = {
        "quote": str(quotes[_]),
        "author": str(authors[_]),
        "tags": str(tags[_])
    }
    json_str = json.dumps(info)
    class User:
        def __init__(self, d):
            self.__dict__ = d
    user = json.loads(json_str, object_hook=User)
    print(f"Quote: {user.quote}")
    print(f"Author: {user.author}")
    print(f"Tags: {user.tags}")
    print('-------------------')

# Word-and-Quote-Crawler
The Crawler goes on to a website and finds quotes on the specific website and it prints them and it can also find the number of times a word has occurred in the text.

<img width="440" height="466" alt="image" src="https://github.com/user-attachments/assets/5bace2a2-93b5-46c8-a242-43c00cecd300" />

I made a python code which uses the website http://quotes.toscrape.com/ to find word occurrences and quotes based on their index and also printing all of them. 

For it to work you need to the website http://quotes.toscrape.com/ as the url otherwise, it may not work. 
[https://youtu.be/2tIYbYY4go4] This is the YouTube video to watch it working.

### libraries

It uses 5 main libraries: requests, BeautifulSoup, re, json, and time.

~~~
import time
import requests
import re
from bs4 import BeautifulSoup
import json
~~~

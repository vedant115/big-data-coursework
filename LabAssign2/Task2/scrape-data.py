import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://en.wikipedia.org/wiki/Indian_Institute_of_Information_Technology,_Allahabad"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Extract text content from the page (strip unnecessary whitespace and tags)
page_text = soup.get_text()

# Limit the number of characters to 1500
page_text = page_text[:1500]

# Save the scraped text to a file
with open('iiit_allahabad_text.txt', 'w', encoding='utf-8') as file:
    file.write(page_text)

print("Text successfully scraped and saved.")

import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime, timedelta

def scrape_ethereum_news():
    # Define the URL of the Ethereum news section on investing.com
    url = 'https://www.investing.com/crypto/ethereum/news'

    # Make a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    print(response.status_code)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all news articles
        news_articles = soup.find_all('article')

        # Open a CSV file in write mode
        with open('ethereum_news.csv', 'w', newline='', encoding='utf-8') as csvfile:
            # Define CSV writer
            writer = csv.writer(csvfile)

            # Write header row
            writer.writerow(['Title', 'Description'])

            # Iterate over news articles
            for article in news_articles:
                # Extract title
                title = article.find('a', class_='title').text.strip()

                # Extract description
                description = article.find('div', class_='textDiv').text.strip()

                # Write title and description to CSV file
                writer.writerow([title, description])

        print("Ethereum news scraped successfully!")
    else:
        print("Failed to retrieve Ethereum news.")

if __name__ == "__main__":
    scrape_ethereum_news()

import requests
from bs4 import BeautifulSoup
import csv

class RedditScraper:
    def __init__(self, url):
        self.url = url
        self.subreddit = " "
        self.title = ""
        self.upvotes =""
        self.comments =""
        self.username =""
        self.timestamp =""
        self.content =""
        self.media  = ""
        self.thread_data = {}
    
    def scrape(self):
        try:
            # Send a GET request to the URL
            page = requests.get(self.url)

            # Parse the HTML content of the page
            soup = BeautifulSoup(page.content, 'html.parser')
        except requests.exceptions.RequestException as e:
            print(f"Error making request: {e}")
            return
        except Exception as e:
            print(f"Error parsing HTML: {e}")
            return

        # Extract the subreddit name from the page
        subreddit_element = soup.find('span', class_='_2wzi-W7JiZ7A6U6aFvfvSR')
        if subreddit_element:
            self.subreddit = subreddit_element.text

        # Extract the thread title from the page
        title_element = soup.find('h1', class_='_eYtD2XCVieq6emjKBH3m')
        if title_element:
            self.title = title_element.text

        # Extract the number of upvotes from the page
        upvotes_element = soup.find('div', class_='_1rZYMD_4xY3gRcSS3p8ODO _3a2ZHWaih05DgAOtvu6cIo _2iiIcja5xIjg-5sI4ECvcV')
        if upvotes_element:
            self.upvotes = upvotes_element

        # Extract the number of comments from the page
        comments_element = soup.find('span', class_='FHCV02u6Cp2zYL0fhQPsO')
        if comments_element:
            self.comments = comments_element.text

        # Extract the username of the person who posted the thread
        username_element = soup.find('a', class_='_2tbHP6ZydRpjI44J3syuqC  _23wugcdiaj44hdfugIAlnX oQctV4n0yUb0uiHDdGnmE')
        if username_element:
            self.username = username_element.text

        # Extract the timestamp of the thread
        timestamp_element = soup.find('time', class_='_2VF2J19pUIMSLJFky-7PEI')
        if timestamp_element:
            self.timestamp = timestamp_element.text

        # Extract the content of the thread
        content_element = soup.find('div', class_='_3AStxql1mQsrZuUIFP9xSg s1y8gf4b-0 gXUyBJ')
        if content_element:
            self.content = content_element
        
        media_url = soup.find('img', class_='_2_tDEnGMLxpM6uOa2kaDB3 ImageBox-image media-element _1XXWObl-3b9tPy64oaG6fax')
        self.media = media_url.get('source') if media_url else None

    def to_csv(self, filename):
     with open(filename, 'w') as file:
            file.write(f"{self.subreddit},{self.title},{self.upvotes},{self.comments},{self.media}\n")

# Create a RedditScraper object with the given URL
scraper = RedditScraper('https://www.reddit.com/r/chennai/comments/z8u42i/what_do_you_guys_think_about_people_who_feed/')

# Scrape the data from the page
scraper.scrape()

# Write the data to a CSV file
scraper.to_csv('redditgahana.csv')
###

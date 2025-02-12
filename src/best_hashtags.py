import requests
from bs4 import BeautifulSoup
import random

class BestHashtags:
    def __init__(self):
        self.base_url = "https://best-hashtags.com/hashtag/{}/"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }

    def get_hashtags(self, search_word, quantity=30, ordered=True):
        url = self.base_url.format(search_word)
        response = requests.get(url=url, headers=self.headers)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            hashtags = soup.find_all('p1')
            
            hashtag_list = []
            for tag in hashtags:
                hashtag_list.extend(tag.text.split())
            
            if ordered:
                hashtag_list = hashtag_list[:quantity]
            else:
                hashtag_list = random.sample(hashtag_list, min(quantity, len(hashtag_list)))
            
            return hashtag_list
        else:
            print(f"Failed to retrieve data: {response.status_code}")
            return []

if __name__ == '__main__':

    word_to_search = 'music'
    
    scraper = BestHashtags()
    print(scraper.get_hashtags(word_to_search, quantity=30, ordered=True))
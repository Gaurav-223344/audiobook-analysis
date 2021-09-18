import requests
import numpy as np
from bs4 import BeautifulSoup

class AudiobookScraping:
        
        def __init__(self):
            pass
    
        
        def url_creation(self,page_no):
          template = f'https://www.audiobooks.com/browse/listType/list/page/{page_no}'
          return template
      
        
        def extract_info(self,item):
          
          item_url = item.find('div','col_two_third').a.get('href')
        
          item_respose = requests.get(item_url)
          item_soup = BeautifulSoup(item_respose.text,'html.parser')
        
          # To scrap Audiobook title
          try:
            title = item_soup.find('h1','audiobookTitle').text.strip()
          except AttributeError:
            title = np.nan
        
          # To scrap Audiobook auther
          try:
            auther = item_soup.find('h4','book-written-by').span.text.strip()
          except AttributeError:
            auther = np.nan
        
          # To scrap Audiobook narrater
          try:
            narrater = item_soup.find('h4','book-narrated-by').span.text.strip()
          except AttributeError:
            narrater = np.nan
        
          # to scrap price of audiobook
          try:
            price = item_soup.find('div','fleft bookActions__button buy-button ').p.text[5:].strip()
          except AttributeError:
            price = np.nan
        
          # to scap publishing date of audiobook
          try:
            date = item_soup.find('h4','book-published-by').span.text.strip()
          except AttributeError:
            date = np.nan
        
          # to scrap time duration of audiobook
          try:
            duration = item_soup.find('h4','book-duration').span.text.strip()
          except AttributeError:
            duration = np.nan
        
          # to scrap how many listeners rating this book
          try:
            book_reviews = item_soup.find('h4','book-rating-header').span.text.strip()[1:-1]
          except AttributeError:
            book_reviews = np.nan
        
          # to scrap book rating
          try:
            book_ratings = item_soup.find('div','total-book-rating book-rating').get('data-score')
          except AttributeError:
            book_ratings = np.nan
        
          # to scrap how many listeners rating this narreter
          try:
            narreter_reviews = item_soup.find('h4','narrator-rating-header').span.text.strip()[1:-1]
          except AttributeError:
            narreter_reviews = np.nan
          
          # to scrap narreter rating
          try:
            narreter_ratings = item_soup.find('div','total-narrator-rating narrator-rating').get('data-score')
          except AttributeError:
            narreter_ratings = np.nan
        
          # to scrap genre
          try:
            genre = []
          except AttributeError:
            genre = np.nan
          for i in range(0,6,1):
            id = 'genre_'+ str(i)
            try:
              value = item_soup.find('div',{"id":id}).text
              genre.append(value)
            except AttributeError:
              break
    
          # to scrap audiobook summery
          try:
            summery = item_soup.find('div','book-description').text.strip()
          except AttributeError:
            summery = np.nan
        
          record = (title,auther,narrater,price,date,duration,book_reviews,book_ratings,narreter_reviews,narreter_ratings,genre,summery,item_url)
          return record
    

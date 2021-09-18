from AudioBookScraper import AudiobookScraping
from bs4 import BeautifulSoup
import requests
import csv


def main():
    
    scraper = AudiobookScraping()
    print("There are total 5000 pages in website and each page contain 20 audiobooks. So you need to decide that which page to start and how many pages you want to scrape.")
    start_page = int(input("Enter Starting page no : "))
    num = int(input("Enter how many pages you want to scrape : "))
    
    end_page = start_page + num
    
    records = []

    for pg in range(start_page,end_page,1):       

        template = scraper.url_creation(pg)
        response = requests.get(template)
        soup = BeautifulSoup(response.text,'html.parser')
    
        items = soup.find_all('li','col_full clearfix')
        if len(items) > 0 :
          for item in items:
            record = scraper.extract_info(item)
            records.append(record)
        else:
          break
  
    with open('Audiobook'+str(start_page)+'_to_'+str(end_page-1)+'.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['title','auther','narrater','price','date','duration','book_reviews','book_ratings','narreter_reviews','narreter_ratings','genre','summery','Url'])
        writer.writerows(records)
        
if __name__=="__main__":
    main()
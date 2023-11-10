from background_task import background

import requests
from bs4 import BeautifulSoup
import time
import urllib.parse
from .models import Article
from django.utils import timezone

@background(schedule=60*10)
def crawl_news():
    base_url = "https://finance.naver.com"
    user_agent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

    news_data = {}
    for i in range(1, 4):
        try:
            res = requests. get(f"{base_url}/news/mainnews.naver?&page={i}", user_agent)
            res.raise_for_status()

            soup = BeautifulSoup(res.text, "html.parser")
    
            news_list = soup.find("ul", class_="newsList")
            titles = news_list.select("li dl dd:nth-of-type(1) a")
            
            for title in titles:
                full_url = urllib.parse.urljoin(base_url, title["href"])
                news_data[title.text.strip()] = full_url
                new_object = Article.objects.create(headline=title.text.strip(), article_url=full_url, crawling_time=timezone.now())

            time.sleep(0.5)
        
        except requests.exceptions.HTTPError as errh:
            print ("Http Error:",errh)
        except requests.exceptions.ConnectionError as errc:
            print ("Error Connecting:",errc)
        except requests.exceptions.Timeout as errt:
            print ("Timeout Error:",errt)
        except requests.exceptions.RequestException as err:
            print ("OOps: Something Else",err)
            
    return news_data




@background(schedule=60*10)
def crawl_chart():
    pass

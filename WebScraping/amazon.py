# import requests
# from bs4 import BeautifulSoup


# class amazonScrapper:
    
#     headers = {
#         "authority": "www.amazon.com",
#         "pragma": "no-cache",
#         "cache-control": "no-cache",
#         "dnt": "1",
#         "upgrade-insecure-requests": "1",
#         "user-agent": "Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36",
#         "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#         "sec-fetch-site": "none",
#         "sec-fetch-mode": "navigate",
#         "sec-fetch-dest": "document",
#         "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
#     }
    
#     def getdata(self,url):
#         r = requests.get(url, headers=self.headers)
#         return r.text
    
#     def cus_rev(self,soup):
#         # find the Html tag
#         # with find()
#         # and convert into string

#         data_str = ""

    
#         for item in soup.find_all("div", class_="a-expander-content \
#         reviewText review-text-content a-expander-partial-collapse-content"):
#             print(item)
#             data_str = data_str + item.get_text()
    
#         result = data_str.split("\n")
#         return (result)
    
    
#     def cus_data(self,soup):
#         # find the Html tag
#         # with find()
#         # and convert into string
#         data_str = ""
#         cus_list = []
    
#         for item in soup.find_all("span", class_="a-profile-name"):
#             data_str = data_str + item.get_text()
#             cus_list.append(data_str)
#             data_str = ""
#         return cus_list



#     def html_code(self,url):
#     # pass the url
#     # into getdata function
#         htmldata = self.getdata(url)
#         soup = BeautifulSoup(htmldata, 'html.parser')
#         print(soup)

#         output = self.cus_data(soup)

    
#         # display html code
#         return (output)
    
# test = amazonScrapper()
# print(test.html_code("https://www.amazon.com/ASUS-ROG-Strix-Gaming-Laptop/product-reviews/B0BV7XQ9V9"))
  
  
from amazon_product_review_scraper import amazon_product_review_scraper

review_scraper = amazon_product_review_scraper(amazon_site="amazon.com", product_asin="B0BV7XQ9V9")
reviews_df = review_scraper.scrape()
print(reviews_df.head(5))
reviews_df.to_csv("out.csv")




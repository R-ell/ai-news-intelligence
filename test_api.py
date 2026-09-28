import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()

#q= "artificail intelligence"






def get_news(topic):
    new_format=[]
    
    
    api_key= os.getenv("API_key")
    
    
    param={
        "apiKey": api_key,

        "q":topic
    }
    r = requests.get("https://newsapi.org/v2/everything",params=param,)
    
    data=r.json()
    article_list=data["articles"]
    for article in article_list:

        article_format={

            "title":article["title"],
            "source":article["source"]["name"],
            "url":article["url"],
            "date_pub":article["publishedAt"]
        }
        #print(article_format["title"])
       # print(article_format["source"])
        #print(article_format["url"])
        #print(article_format["date_pub"])
        new_format.append(article_format)

    return new_format
"""""
response={
    "art":data["articles"][0],
    "art_name": data["name"][0],
    "author":data["author"][0]




}
"""




"""""
return_data=get_news(data)
print(len(return_data))
print(return_data[0])
print(return_data[0]["title"])

"""

                                                                                                                                                                                                                                                      

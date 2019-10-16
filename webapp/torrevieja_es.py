from flask import current_app
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_news():
    """
    Скачивание всех новостей с сайта и их парсинг
    Возвращает словарь с новостями либо False
    """
    url = "http://www.torrevieja.es/sal/index.aspx"
    try:
        html = requests.get(url).text

        soup = BeautifulSoup(html, 'html.parser')
        news_all = soup.find("div", class_="NotiPorta1")
      
        news_title = news_all.findAll("p", { "class" : ["WATNTi","WATATi"]})
        news_shorttext = news_all.findAll("td",class_="WATNotEntradilla")
        news_url = news_all.findAll("span",class_="WATemail")
        news_fecha = news_all.findAll("span",class_="FechaNoti")

        list_news = []
        for i in range(len(news_shorttext)):
            one_news = {}
            one_news["shorttextEs"] = str(news_shorttext[i].text).strip()
            one_news["titleEs"] = str(news_title[i].text).strip()
            one_news["url"] = f'http://www.torrevieja.es{news_url[i].find("a")["href"]}'
            try:
                one_news["fecha"] = datetime.strptime(str(news_fecha[i].text),"%d/%m/%Y")#03/10/2019
            except:
                one_news["fecha"] = datetime.now()
            list_news.append(one_news)
        return list_news
    except BaseException as e: 
        print(str(e))
        return False

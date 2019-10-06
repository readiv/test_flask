from flask import current_app
import requests
from bs4 import BeautifulSoup
from datetime import datetime

def get_translate(text,lang='es-ru'):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
    if text:
        try:
            text_translate = requests.post(url, data={'key': current_app.config["API_KEY_YA_TRANSLATE"], 'text': text, 'lang': lang})
            text_translate = text_translate.json()["text"][0]
            return text_translate
        except BaseException as e:
            print("############################################")
            print(f"{lang}\n{text}") 
            print(str(e))
    return text

def get_news():
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

if __name__=="__main__":
    news_list = get_news()
    if news_list:
        print(news_list)
    #print(get_translate("L COINCIDIENDO CON LA CELEBRACIÓN DE HALLOWEEN"))
    pass
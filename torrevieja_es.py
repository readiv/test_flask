import requests
from bs4 import BeautifulSoup
from setting import API_KEY_YA_TRANSLATE

def get_translate(text,lang='es-ru'):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
    try:
        text_translate = requests.post(url, data={'key': API_KEY_YA_TRANSLATE, 'text': text, 'lang': lang})
        text_translate = text_translate.json()["text"][0]
        return text_translate
    except BaseException as e: 
        print(str(e))
        return text

def get_news(url):
    try:
        html = requests.get(url).text

        soup = BeautifulSoup(html, 'html.parser')
        news_all = soup.find("div", class_="NotiPorta1")

        news_shorttext = news_all.findAll("td",class_="WATNotEntradilla")
        news_url = news_all.findAll("span",class_="WATemail")
        news_fecha = news_all.findAll("span",class_="FechaNoti")

        list_news = []
        for i in range(len(news_shorttext)):
            one_news = {}
            one_news["shorttext"] = get_translate(str(news_shorttext[i].text).strip(),"es-ru")
            # one_news["shorttext"] = str(news_shorttext[i].text).strip()
            one_news["url"] = f'http://www.torrevieja.es{news_url[i].find("a")["href"]}'
            one_news["fecha"] = str(news_fecha[i].text)
            list_news.append(one_news)
        return(list_news)
    except BaseException as e: 
        print(str(e))
        return False

if __name__=="__main__":
    pass
    # news_list = get_news("http://www.torrevieja.es/sal/index.aspx")
    # if news_list:
    #     print(news_list)
    #print(get_translate("LA CONCEJALÍA DE JUVENTUD ORGANIZA UN VIAJE A PORTAVENTURA 2019 COINCIDIENDO CON LA CELEBRACIÓN DE HALLOWEEN"))
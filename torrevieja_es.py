import requests
from bs4 import BeautifulSoup

def get_translate(text):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
    key = 'trnsl.1.1.20191001T224658Z.a13ec0f352090231.a43d8c6eba456e60589dc2bebe1c55ba966b783f'
    lang = 'es-ru'
    r = requests.post(url, data={'key': key, 'text': text, 'lang': lang}).json()
    print(r["text"][0].strip())
    return r["text"][0].strip()

def get_news(url):
    try:
        html = requests.get(url).text

        soup = BeautifulSoup(html, 'html.parser')
        news_all = soup.find("div", class_="NotiPorta1")

        news_shorttext = news_all.findAll("td",class_="WATNotEntradilla")
        news_url = news_all.findAll("span",class_="WATemail")
        news_fecha = news_all.findAll("span",class_="FechaNoti")

        result = []
        for i in range(len(news_shorttext)):
            result_uno = {}
            result_uno["shorttext"] = get_translate(str(news_shorttext[i].text))
            result_uno["url"] = f'http://www.torrevieja.es{news_url[i].find("a")["href"]}'
            result_uno["fecha"] = str(news_fecha[i].text)
            result.append(result_uno)
        return(result)
    except:
        print('Сетевая ошибка')
        return False

if __name__=="__main__":
    # news_list = get_news("http://www.torrevieja.es/sal/index.aspx")
    # if news_list:
    #     print(news_list)
    get_translate("LA CONCEJALÍA DE JUVENTUD ORGANIZA UN VIAJE A PORTAVENTURA 2019 COINCIDIENDO CON LA CELEBRACIÓN DE HALLOWEEN")
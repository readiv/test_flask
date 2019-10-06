from flask import current_app
from webapp.model import db,News
from webapp.torrevieja_es import get_news,get_translate
from webapp.weather import update_weather


def save_news_db(titleEs, url, fecha, shorttextEs, textEs):
    news_exists = News.query.filter(News.url == url).count()
    if not news_exists:        
        new_news = News(titleEs=titleEs, titleRu=get_translate(titleEs,"es-ru"), titleEn=get_translate(titleEs,"es-en"),
                        url=url, fecha=fecha, 
                        shorttextEs=shorttextEs,shorttextRu=get_translate(shorttextEs,"es-ru"),shorttextEn=get_translate(shorttextEs,"es-en"),
                        textEs=textEs,textRu=get_translate(textEs,"es-ru"),textEn=get_translate(textEs,"es-en"))
        db.session.add(new_news)
        db.session.commit()


def update_all_info():
    update_weather()
    list_news = get_news()
    if list_news:
        for one_news in list_news:
            save_news_db(one_news["titleEs"],one_news["url"],one_news["fecha"],one_news["shorttextEs"],"")
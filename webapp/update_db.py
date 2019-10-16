from flask import current_app
from webapp.model import db,News
from webapp.torrevieja_es import get_news
from webapp.tiempo import tiempo_update
from webapp.translate import get_translate


def save_news_db(titleEs, url, fecha, shorttextEs, textEs):
    """
    Если этой новости нет, то перевести и добавить в БД
    """
    news_exists = News.query.filter(News.url == url).count()
    if not news_exists:        
        new_news = News(titleEs=titleEs, titleRu=get_translate(titleEs,"es-ru"), titleEn=get_translate(titleEs,"es-en"),
                        url=url, fecha=fecha, 
                        shorttextEs=shorttextEs,shorttextRu=get_translate(shorttextEs,"es-ru"),shorttextEn=get_translate(shorttextEs,"es-en"),
                        textEs=textEs,textRu=get_translate(textEs,"es-ru"),textEn=get_translate(textEs,"es-en"))
        db.session.add(new_news)
        db.session.commit()


def update_all_info():
    """
    Для вызова по таймеру
    Обновить погоду
    Обновить новости
    """
    tiempo_update()
    list_news = get_news()
    if list_news:
        for one_news in list_news:
            save_news_db(one_news["titleEs"],one_news["url"],one_news["fecha"],one_news["shorttextEs"],"")
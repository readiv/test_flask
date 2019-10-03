from flask import Flask,render_template
from webapp.weather import weather_by_city
from webapp.torrevieja_es import get_news


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("setting.py")
    @app.route("/")
    def hello():
        wather = weather_by_city(app.config["WEATHER_DEFAULT_CITY"])
        # print(wather)
        list_news = get_news("http://www.torrevieja.es/sal/index.aspx")
        # print(list_news)
        if wather and list_news:
            return render_template('index.html', weather=wather, list_news = list_news,len_list_news=len(list_news))
        else: 
            return "Сервер временно недоступен. Обновляются данные!"

    return app



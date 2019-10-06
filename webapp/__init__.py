from flask import Flask,render_template
from webapp.weather import weather_by_city
from webapp.model import db, News

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("setting.py")
    db.init_app(app)

    @app.route("/")
    def hello():
        wather = weather_by_city(app.config["WEATHER_DEFAULT_CITY"])
        list_news = News.query.order_by(News.fecha.desc()).all()
        if wather and list_news:
            return render_template('index.html', weather=wather, list_news = list_news,lang = app.config["OUT_LANG"])
        else: 
            return "Сервер временно недоступен. Обновляются данные!"

    return app



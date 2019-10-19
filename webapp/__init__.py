from flask import Flask, render_template, request
from flask_babel import Babel
from webapp.model import db, News
from webapp.update_db import update_all_info


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("setting.py")
    db.init_app(app)

    Babel(app)

    @app.route("/")
    def index():
        lang = str(request.args.get("lang"))
        if lang.find("ru") != -1:
            app.config['BABEL_DEFAULT_LOCALE'] = "ru"
        elif lang.find("en") != -1:
            app.config['BABEL_DEFAULT_LOCALE'] = "en"
        elif lang.find("es") != -1:
            app.config['BABEL_DEFAULT_LOCALE'] = "es"

        if not app.config.get("temp_C"):
            update_all_info()
        list_news = News.query.order_by(News.fecha.desc()).all()

        if list_news:
            return render_template("index.html",
                                   temp_C=app.config["temp_C"],
                                   FeelsLikeC=app.config["FeelsLikeC"],
                                   list_news=list_news,
                                   lang=app.config.get("BABEL_DEFAULT_LOCALE"))
        else:
            return render_template('error.html')
    return app

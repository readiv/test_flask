from flask import Flask,render_template,request
from webapp.model import db, News
from webapp.update_db import update_all_info

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("setting.py")
    db.init_app(app)

    @app.route("/")
    def index():
        lang = str(request.args.get("lang"))
        if lang.find("ru") != -1:
            lang = "ru"
        elif lang.find("en") != -1:
            lang = "en"
        else:
            lang = "es"

        frazes_list =   {"ru":  {"title":"Торревьеха",
                                 "ahora":"Сейчас в Торревьехе",
                                 "grados":"градусов",
                                 "siente":"Ощущается как",
                                 "disponible":"Сервис погоды временно недоступен",
                                 "detalles":"Подробнее ..."
                                },
                         "es":  {"title":"Torrevieja",
                                 "ahora":"Ahora en Torrevieja",
                                 "grados":"grados",
                                 "siente":"Se siente como",
                                 "disponible":"El servicio meteorológico no está disponible temporalmente",
                                 "detalles":"Más detalles »"
                                },
                         "en":  {"title":"Torrevieja",
                                 "ahora":"Now in Torrevieja",
                                 "grados":"degrees",
                                 "siente":"Feels like",
                                 "disponible":"Weather service is temporarily unavailable",
                                 "detalles":"View details »"
                                }
                        }   

        if not app.config.get("temp_C"):
            update_all_info()
        list_news = News.query.order_by(News.fecha.desc()).all()
        # print(request.args.get)
        if list_news:
            return render_template('index.html', temp_C=app.config["temp_C"], FeelsLikeC=app.config["FeelsLikeC"], 
                                    list_news = list_news,lang=lang,frazes=frazes_list[lang])
        else: 
            return render_template('error.html')
    
    return app



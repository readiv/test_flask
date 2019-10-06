
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'webapp.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

WEATHER_URL = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
WEATHER_DEFAULT_CITY = "Torrevieja"
API_KEY_WEATHER = "025930d8fddd4f4c893183751193009"

API_KEY_YA_TRANSLATE = 'trnsl.1.1.20191001T224658Z.a13ec0f352090231.a43d8c6eba456e60589dc2bebe1c55ba966b783f'

OUT_LANG="en"



    
from flask import current_app
import requests

def weather_by_city(city_name):
    weather_url = current_app.config["WEATHER_URL"]
    params = {
        "key": current_app.config["API_KEY_WEATHER"],
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lang": "ru"
    }
    try:
        result = requests.get(weather_url, params=params).json()
        return result['data']['current_condition'][0]
    except (requests.RequestException,IndexError,TypeError):
        return False  

def update_weather():
    weather_ahora = weather_by_city(current_app.config["WEATHER_DEFAULT_CITY"]) 
    try:
        current_app.config["temp_C"] = weather_ahora["temp_C"]
        current_app.config["FeelsLikeC"] = weather_ahora["FeelsLikeC"]
        # print(f"update_weather {current_app.config['temp_C']}")
    except:
        current_app.config["temp_C"] = False

if __name__=="__main__":
    print(weather_by_city('Torrevieja'))
from flask import current_app
import requests


def tiempo_en_ciudad(city_name):
    """
    Возвращает погоду в городе city_name
    Настройки хранятся в setting.py
    Затем подгружаются в конфиг flask
    Возврат либо словарь с данными, либо False
    """
    tiempo_url = current_app.config["TIEMPO_URL"]
    params = {
        "key": current_app.config["TIEMPO_API_KEY"],
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lang": "ru"
    }
    try:
        tiempo_data = requests.get(tiempo_url, params=params).json()
        return tiempo_data['data']['current_condition'][0]
    except (requests.RequestException, IndexError, TypeError):
        return False


def tiempo_update():
    """
    Должна обновить текущюю погоду
    Планируется для вызовов в очереди или по таймеру
    """

    tiempo_ahora = tiempo_en_ciudad(current_app.config["TIEMPO_DEFAULT_CITY"])
    if tiempo_ahora:
        temp_C = tiempo_ahora.get("temp_C")
        FeelsLikeC = tiempo_ahora.get("FeelsLikeC")

        if temp_C is not None and FeelsLikeC is not None:
            current_app.config["temp_C"] = temp_C
            current_app.config["FeelsLikeC"] = FeelsLikeC
            return

    current_app.config["temp_C"] = False
    current_app.config["FeelsLikeC"] = False

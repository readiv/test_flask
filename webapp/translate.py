from flask import current_app
import requests

def get_translate(text,lang='es-ru'):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
    if text:
        try:
            text_translate = requests.post(url, data={'key': current_app.config["API_KEY_YA_TRANSLATE"], 'text': text, 'lang': lang})
            text_translate = text_translate.json()["text"][0]
            return text_translate
        except BaseException as e:
            print("############################################")
            print(f"{lang}\n{text}") 
            print(str(e))
    return text
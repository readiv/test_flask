from flask import Flask,render_template
from weather import weather_by_city
from torrevieja_es import get_news

app = Flask(__name__)

@app.route("/")
def hello():
    wather = weather_by_city("Torrevieja")
    # print(wather)
    list_news = get_news("http://www.torrevieja.es/sal/index.aspx")
    # print(list_news)
    if wather and list_news:
        return render_template('index.html', weather=wather, list_news = list_news,len_list_news=len(list_news))
    else: 
        return "Сервер временно недоступен. Обновляются данные!"


if __name__=="__main__":
    app.run(debug=True)

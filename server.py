from flask import Flask,render_template
from weather import weather_by_city
from torrevieja_es import get_news
import threading 
import time

wather = False
list_news = False
lock = threading.Lock()
 
app = Flask(__name__)

def updatedata():
    global wather,list_news
    while True:
        lock.acquire()
        try:
            wather = weather_by_city("Torrevieja")
            # print(wather)
            list_news = get_news("http://www.torrevieja.es/sal/index.aspx")
            # print(list_news)
        finally:
            lock.release()
        time.sleep(600)

@app.route("/")
def hello():
    global wather,list_news
    lock.acquire()
    try:
        # print(wather)
        # print(list_news)
        if wather and list_news:
            return render_template('index.html', weather=wather, list_news = list_news,len_list_news=len(list_news))
        else: return "Сервер временно недоступен. Обновляются данные!"
    finally:
        lock.release()

if __name__=="__main__":
    t = threading.Thread(target=updatedata)
    t.daemon = True
    t.start()

    app.run(debug=True)

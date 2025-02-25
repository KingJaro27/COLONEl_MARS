from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
@app.route("/index")


def index():
    return "И на Марсе будут яблони цвести!"

def home():
    return "Миссия Колонизация Марса"

if __name__ == "__main__":
    app.run(port=7016, host="127.0.0.1")

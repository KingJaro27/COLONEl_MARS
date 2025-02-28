from flask import Flask, url_for, render_template

app = Flask("mars")

@app.route("/")
@app.route("/index")
def index():
    user = "Ученик Яндекс.Лицея"
    return render_template("index.html", title="Домашняя страница", username=user)


app.run()

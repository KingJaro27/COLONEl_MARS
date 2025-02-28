from flask import Flask, url_for, render_template

app = Flask("mars")


@app.route("/")
@app.route("/index")
def index():
    user = "Ученик Яндекс.Лицея"
    return render_template("index.html", username=user)


@app.route("/training/<prof>")
def training(prof):
    return render_template("training.html", prof=prof)


app.run(port=7016, host="127.0.0.1")

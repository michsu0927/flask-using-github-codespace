from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    t = "Hi github"
    return render_template("index.html", title=t)
#could

from urllib import request
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        return render_template("index.html", placeholder_text = "Hello from POST method")
    if (request.method == 'GET'):
        return render_template("index.html", placeholder_text = "Hello from GET method")

@app.route("/submit")
def submit():
    return "Hello from submit page"

if __name__ == '__main__':
    app.run()

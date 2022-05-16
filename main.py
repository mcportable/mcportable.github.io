from flask import Flask, render_template, send_file, send_from_directory
from datetime import date

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", year=date.today().year)

@app.route('/img/<image>')
def img(image):
    return send_file("images/"+str(image))

@app.route('/css')
def css():
    return send_file("style.css")

@app.route('/file/<image>')
def files(file):
    return send_file("files/"+str(file))

if __name__ == '__main__':
    app.run(debug=True, port=80)
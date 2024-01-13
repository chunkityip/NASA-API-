from flask import Flask, render_template, url_for
import requests
from flask_fontawesome import FontAwesome
#4 libraries, flask, requests, flask_fontawesome and fontawesome

app = Flask(__name__)
fa = FontAwesome(app)

url = requests.get(
    'https://api.nasa.gov/planetary/apod?api_key=iBeT2hXG8tezilCqlJ5IXkNpTPWBFpB95bo72qyh', timeout=60)
text = url.json()
image = text['url']
name = text['copyright']
dt = text['date']
ti = text['title']
expl = text['explanation']

info = [{'title': ti,
         'name': name,
         'day': dt,
         'detail': expl,
         'image': image}]

#using dummy data to jinja2


@app.route("/")
@app.route("/home")
def home():
    return render_template('index.html', posts=info)


@app.route('/index', methods=['GET', 'POST'])
def lionel():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)



from flask import Flask ,request,jsonify
app = Flask(__name__)

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'published': '1975'}
]

@app.route("/")
def home():
    return "Hello, Flask!, <h1>My first demo app</h1>,<p>everything is possible</p>"

@app.route("/app" , methods=['GET'])
def go():
    return jsonify(books)
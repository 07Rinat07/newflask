from flask  import Flask

app = Flask(__name__)

@app.route("/index")
@app.route("/")
def index():
    return "<h1> ГЛАВНАЯ СТРАНИЦА</h1>"



@app.route("/about")
def about():
    return "<h1> СТРАНИЦА О НАС</h1>"

if __name__ == '__main__':
    app.run(debug=True)
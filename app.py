from flask  import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newflask.db'

db = SQLAlchemy(app)

app = Flask(__name__)  # 👈 static автоматически = ./static/

class Post(db.Model):  # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(300), nullable=False)
    text= db.Column(db.Text, nullable=False)

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/create")
def create():
        return render_template('create.html')



@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
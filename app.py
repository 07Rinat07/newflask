from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect

app = Flask(__name__)  # ✅ создаем ОДИН раз!
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///newflask.db'
db = SQLAlchemy(app)

# ----- Модель -----
class Post(db.Model):  # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)

# ----- Роуты -----
@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/create", methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']

        post = Post(title=title, text=text)

        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/')
        except:
            return 'При добавлении записи произошла ошибка!'
    else:
        return render_template('create.html')


@app.route("/about")
def about():
    return render_template('about.html')


# ----- Запуск -----
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # ✅ создадим таблицы при запуске
    app.run(debug=True)

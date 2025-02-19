from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from login_and_registr import login

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
db =  SQLAlchemy(app)


@app.route('/index')
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/posts")
def posts():
    posts = Post.query.all()
    return render_template("posts.html", posts=posts)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    text = db.Column(db.Text, nullable=False)

@app.route('/create', methods=["POST", "GET"])
def create():
    if request.method == "POST":
        title = (request.form['title'])
        text = (request.form.getlist('text')[0])

        post = Post(title=title, text=text)
        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/index')
        except:
            return "При добавлении статьи произошла ошибка!"
    else:
        return render_template("create.html")



@app.route("/about_project")
def about_project():
    return render_template("about_project.html")



@app.route("/logins", methods=["POST", "GET"])
def logins():
    return login()


if __name__ == '__main__':
    app.run(debug=True)

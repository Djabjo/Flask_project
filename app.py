from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about_project")
def about_project():
    return render_template("about_project.html")

if __name__ == '__main__':
    app.run(debug=True)

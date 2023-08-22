from flask import Flask, flash, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "8t872tr13cucsjcsco98*&^%$#@s"


@app.route("/")
def hello():
  return "hello World"


@app.route("/path/<path:subpath>")
def path(subpath):
  return subpath


@app.route('/login', methods=['GET', 'POST'])
def login():
  error = None
  if request.method == "POST":
    if request.form['user'] != 'admin' or request.form['pass'] != 'try':
      error = "invalid credentials"
    else:
      flash("hogya bhai")
      user = request.form['user']
      return loggedin(user)
  return render_template('login.html', error=error)


@app.route('/hello/<string:name>')
def helo(name='jayesh'):
  return render_template('try.html.jinja', name=name)


def dologin():
  return render_template('login.html')


def loggedin(user):
  return render_template('logged.html', username=user)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

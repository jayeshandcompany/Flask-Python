from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def hello():
  return "hello World"


@app.route("/path/<path:subpath>")
def path(subpath):
  return subpath


@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'GET':
    return dologin()
  if request.method == "POST":
    return loggedin()
@app.route('/hello/<string:name>')
def helo(name='jayesh'):
  return render_template('try.html.jinja',name=name)

def dologin():
  return render_template('login.html')


def loggedin():
  return render_template('logged.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, Valery"


@app.route('/about')
def about():
    return "About us"


if __name__ == "__main__":
    app.run(debug=True)

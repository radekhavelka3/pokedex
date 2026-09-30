from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Úvodní stránka</h1>"

@app.route("/about")
def about():
    return "<h1>O aplikaci</h1>"

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask

app = Flask(__name__)


@app.route("/")
def fortune():
    return "<p>Fortune-of-the-Day Coming Soon<p>"

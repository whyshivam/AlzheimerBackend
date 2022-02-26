from flask import Flask, jsonify, render_template
import os

app = Flask(__name__)


@app.route("/test", methods=["GET"])
def test():
    return jsonify({"greetings": "Hello world"})


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

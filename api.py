from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/test", methods=["GET"])
def test():
    return jsonify({"greetings": "Hello world"})


if __name__ == "__main__":
    app.run(debug=True)

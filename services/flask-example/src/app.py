from flask import Flask, jsonify


app = Flask(__name__)

@app.route("/", methods=["GET"])
def route_root():
    return jsonify(
        service="flask-example",
        version="0.1.0",
    )

from flask import Flask, request

# Flask + Redis + NGINX + MySQL

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return "Hello World"


@app.route("/micro",methods=["GET"])
def get_req():
    return {"ok":"GET"}


@app.route("/micro", methods=["POST"])
def post_req():
    return {"ok": "POST"}


@app.route("/micro", methods=["PATCH"])
def patch_req():
    return {"ok": "PATCH"}


@app.route("/micro", methods=["DELETE"])
def del_req():
    return {"ok": "DELETE"}


app.run(host="0.0.0.0", port=5000, debug=True)

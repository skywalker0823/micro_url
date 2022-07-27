from flask import Flask, request

# Flask + Redis + NGINX + MySQL

app = Flask(__name__)

@app.route("/micro",methods=["GET"])
def get_req():
    return {"ok":"GET"}


@app.route("/micro", methods=["POST"])
def get_req():
    return {"ok": "POST"}


@app.route("/micro", methods=["PATCH"])
def get_req():
    return {"ok": "PATCH"}


@app.route("/micro", methods=["DELETE"])
def get_req():
    return {"ok": "DELETE"}


app.run(port=5000, debug=True)

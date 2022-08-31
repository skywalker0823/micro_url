from flask import Flask, request, render_template as rt

#縮網址服務
# Flask + Redis + NGINX + MySQL

app = Flask(__name__, static_folder="static", static_url_path="/",template_folder="templates")


@app.route("/", methods=["GET"])
def index():
    return rt("index.html")

#當有人鍵入短網址，會先到這邊
@app.route("/micro",methods=["GET"])
def get_req():
    return {"ok":"GET"}

#將想要縮的網址放到這裡
@app.route("/micro", methods=["POST"])
def post_req():
    data = request.get_json()
    print(data["address"])
    #取得對方輸入的長地址
    address = data["address"]
    #去資料庫查詢是否有縮過，若無則產生，有則回覆已持有的
    
    return {"ok": "POST"}


@app.route("/micro", methods=["PATCH"])
def patch_req():
    return {"ok": "PATCH"}


@app.route("/micro", methods=["DELETE"])
def del_req():
    return {"ok": "DELETE"}


app.run(host="0.0.0.0", port=5001, debug=True)
